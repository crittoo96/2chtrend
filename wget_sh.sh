#!/bin/bash

rm -rf kakologs_html
mkdir kakologs_html
while read line
do
wget $line -P ./kakologs_html
done < ./wget_list.txt