#!/bin/bash
grep -e "\'tv\.yuanqi\.\(business\|model\)\(\.[a-z]\+\)\?\.[A-Z]\{1,\}[A-Za-z]\{1,\}\'" -r $1
