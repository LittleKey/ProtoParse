#!/usr/bin/env python
# encoding: utf-8

import subprocess
import sys
import os

"""
gen_info data structure:
    {
        path: {
            # import info
            module: [class, ...],
            ...
        },
        ...
    }

pb_info data structure
    [(filename, classname), ...]
"""

CMD = r"""grep -e "'\(rpc\|vitality\|business\|model\)\(\.[a-z]\+\)\?\.[A-Z]\{1,\}[A-Za-z]\{1,\}'" -r %s"""

FILE_HEADER = """
#!/usr/bin/env python
# encoding: utf-8
"""

FILE_FOOTER = """
if __name__ == '__main__':
    pass
"""

IMPORT_LINE = """from {module_name} import {class_list_name}\n"""

IMPORT_SEP = ', '

INIT_FILE_NAME = "__init__.py"

CURRENT_DIR = '.'

def format_pb_info(info):
    rlt = []
    for line in info.split(','):
        line = line.strip()
        if line != '':
            left, right = line.split(':')
            filename = left.strip()[:-1]
            classname = right.split('=')[1].strip('\'').split('.')[-1]
            rlt.append((filename, classname))

    return rlt

def get_file_base_name_without_extname(filename):
    return '.'.join(os.path.basename(filename).split('.')[:-1])

def gen_init_file(info):
    for path, import_info in info.items():
        # set work dir by ${path}
        with open(os.path.join(CURRENT_DIR, path, INIT_FILE_NAME), 'w') as fp:
            # write file header
            fp.write(FILE_HEADER)
            for module, class_list in import_info.items():
                # write import info
                fp.write(IMPORT_LINE.format(module_name=module,
                                            class_list_name=IMPORT_SEP.join(class_list)))
            #write file footer
            fp.write(FILE_FOOTER)

def pb_info2gen_info(pb_info):
    gen_info = {}
    for filename, classname in pb_info:
        path = os.path.dirname(filename)
        import_info = gen_info.get(path, {})
        module = get_file_base_name_without_extname(filename)
        class_list = import_info.get(module, [])
        class_list.append(classname)

        import_info[module] = class_list
        gen_info[path] = import_info

    return gen_info

def main():
    p = subprocess.Popen(CMD % sys.argv[1], shell=True, stdout=subprocess.PIPE)
    p.wait()
    pb_info = format_pb_info(p.stdout.read())
    gen_init_file(pb_info2gen_info(pb_info))

if __name__ == '__main__':
    main()

