#!/bin/bash

source ~/source_gpu_gromacs.sh

gmx_mpi grompp -f NVT.mdp -c b.gro -p topol.top -n index.ndx -o prod.tpr

export OMP_NUM_THREADS=1

mpiexec -n 1 gmx_mpi mdrun -s prod.tpr -deffnm prod -nsteps 500000 -plumed plumed.dat -pin on -pinoffset 30 -gpu_id 0 
