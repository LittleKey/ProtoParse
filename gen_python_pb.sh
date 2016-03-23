#!/bin/bash
CURRENT_DIR=`pwd`
PATH=$PATH:$CURRENT_DIR
cd $1
protoc --python_out=$CURRENT_DIR vitality/*
