#!/bin/bash

#ファイルであるaには問題の文字列が入っている
#結果がaに出力されるので、もう一回実行するときはaを再設定する必要がある
#勉強用
echo -n "回数を指定してください: "
read input
for((i=0;i<$input;i++))
do    
    file=`base64 -D a`
    cat $file > a
done

cat a
