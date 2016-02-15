#!/usr/bin/env python
# encoding: utf-8

import sys

import tv.yuanqi.business as business
import tv.yuanqi.model as model


if __name__ == '__main__':
    response = business.__getattribute__(sys.argv[1])()
    s = ' '.join(sys.argv[2:])
    response.ParseFromString(
        ''.join(map(lambda s: chr(int(s, 16)), [s[i:i+2] for i in range(0, len(s), 2)])))
    print(response)
