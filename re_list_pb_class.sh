#!/bin/bash
grep -e "'\(vitality\|rpc\|business\|model\)\(\.[a-z]\+\)\?\.[A-Z]\{1,\}[A-Za-z]\{1,\}'" -r $1
