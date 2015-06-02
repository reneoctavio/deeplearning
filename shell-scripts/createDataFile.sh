#!/bin/sh

#  createDataFile.sh
#  
#
#  Created by Rene Octavio Queiroz Dias on 5/18/15.
#

DATA=/Users/reneoctavio/Documents/TorchData/Caltech101/101_ObjectCategories/

cd $DATA

DIR="."

function list_files() {
    if !(test -d "$1")
    then
        echo $1; return;
    fi

    cd "$1"

    for i in *
    do
        if test -d "$i"
        then
            list_files "$i" #recursively list files
            cd ..
        else
            echo "${PWD##*/}/$i ${PWD##*/}" >> $DATA/files.txt; #Display File name and directory
        fi
    done
}

if [ $# -eq 0 ]
then
    list_files .
    exit 0
fi

for i in $*
do
    DIR="$1"
    list_files "$DIR"
    shift 1 #To read next directory/file name
done