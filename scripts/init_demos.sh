#$/bin/bash
for name in `ls src | grep demo`
do
    dipdup -c src/$name/dipdup.yml init --overwrite-types
    dipdup -c src/$name/dipdup.yml -c src/$name/dipdup-docker.yml docker init
done