#!/bin/bash

fullpath=`realpath "$1"`
pattern=".*[0-9]+\.epub"

target=""
for entry in "$fullpath"/*
do
	bn=`basename "$entry"`
	if [[ $bn =~ $pattern ]];
	then
		target=$entry
	fi
done

book="${target%/*}"
book="${book##*/}"
book_pat='[A-Za-z]+ [A-Za-z]+'
[[ $book =~ $book_pat ]]
book="${BASH_REMATCH[0]}"
dir_path=`dirname "$target"`

from="$target"
to="$dir_path/$book.epub"

ebook-convert "$from" "$to"
