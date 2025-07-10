#!/bin/bash

source source_gpu_gromacs.sh
export OMP_NUM_THREADS=1

for i in {1..10}
do 
	cp -r template/ run$i
	cd run$i
	j=$(( 2*i+14 ))
	gmx_mpi grompp -f md.mdp -c unfolded.gro -p topol_01.top -o input.tpr 
	mpiexec -n 1 gmx_mpi mdrun -s input.tpr -deffnm prd_metaD -nsteps 50000000 -plumed plumed.dat -pin on -pinoffset $j -gpu_id 1 &
	cd ..
done

