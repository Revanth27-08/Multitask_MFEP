#!/bin/bash

source ~/source_gromacs_gpu.sh

for i in {1..10}
do
	cp -r template/ run$i
	cd run$i
	sed -i "s/SEED/$i/g" input_md.dat
	plumed ves_md_linearexpansion input_md.dat &
	cd ..
done
