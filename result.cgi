#!/bin/bash

# ヘッダ出力
echo -ne "Content-Type: text/plain; charset=UTF-8\n\n"

# デバッグ用にパラメータを全出力
echo "It works!"

echo "PATH_INFO: $PATH_INFO"
echo "QUERY_STRING: $QUERY_STRING"

PARAMS=$(echo ${QUERY_STRING} | tr '&' '\n' | tr '=' ' ')

# 編成番号は数字のみ
fnum=$(echo "${PARAMS}" | grep 'fnum' | cut -d' ' -f2 | sed 's/[^0-9]//g')

# 列車番号
tnum=$(echo "${PARAMS}" | grep 'tnum' | cut -d' ' -f2 | sed 's/[^ACDGJKL0-9]//g')

# 日付
search_date=$(echo ${PATH_INFO} | sed 's/^\//')

echo "search_date: $search_date"
echo "fnum: $fnum"
echo "tnum: $tnum"
