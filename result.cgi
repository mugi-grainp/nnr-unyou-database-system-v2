#!/bin/bash

echo -ne "Content-Type: text/plain; charset=UTF-8\n\n"

echo "It works!"

echo "PATH_INFO: $PATH_INFO"
echo "QUERY_STRING: $QUERY_STRING"

PARAMS=$(echo ${QUERY_STRING} | tr '&' '\n' | tr '=' ' ')

fnum=$(echo "${PARAMS}" | grep 'fnum' | cut -d' ' -f2 | sed 's/[^0-9]//g')
tnum=$(echo "${PARAMS}" | grep 'tnum' | cut -d' ' -f2)

echo "fnum: $fnum"
echo "tnum: $tnum"
