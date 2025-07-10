#!/bin/bash

#source plumed
source ~/plumed2-master/libtorch/sourceme.sh
source ~/plumed2-master/sourceme.sh

mpiexec -n 8 /home/ray-lab3/cp2k/exe/local/cp2k.popt -i propHBr_pm6_A.inp -o anti-markonikov.log  
