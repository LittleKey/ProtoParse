#!/bin/bash

./gen_python_pb.sh $1
./gen_init_for_import_pb.py tv
touch tv/__init__.py
touch tv/yuanqi/__init__.py
