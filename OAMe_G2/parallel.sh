#!/bin/bash

source ~/source_gpu_gromacs.sh

export OMP_NUM_THREADS=1

for i in {1..10}
do 
	cp -r template run$i
	cd run$i
	j=$(((2*i)+12)) 
	gmx_mpi grompp -f NVT.mdp -c b.gro -p topol.top -n index.ndx -o prod.tpr
	mpiexec -n 1 gmx_mpi mdrun -s prod.tpr -deffnm prod -nsteps 50000000 -plumed plumed.dat -pin on -pinoffset $j -gpu_id 1 &
	cd ..
done
