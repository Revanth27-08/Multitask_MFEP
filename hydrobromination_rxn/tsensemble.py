import numpy as np

stateM_cut_d3 = 2.1
stateM_cut_d5 = 2.8

f2 = open('ts_data/all_data', 'w')

for i in range(1,11):
    f1 = open('ts_data/data_%d'%i,'w')
    l = np.loadtxt('run%d/distances'%i)
    l_flipped = np.flip(l,axis=0)
    for j in range(len(l_flipped)):
        if l_flipped[j,3] > stateM_cut_d3 or l_flipped[j,5] < stateM_cut_d5:
            for k in range(len(l_flipped[j])):
                print(l_flipped[j,k],end=' ',file=f1)
                print(l_flipped[j,k],end=' ',file=f2)
            print(file=f1)
            print(file=f2)
        if l_flipped[j,3] < stateM_cut_d3 and l_flipped[j,5] > stateM_cut_d5:
            break
        else :
            for k in range(len(l_flipped[j])):
                print(l_flipped[j,k],end=' ',file=f1)
                print(l_flipped[j,k],end=' ',file=f2)
            print(file=f1)
            print(file=f2)

    f1.close()
    print('traj_%d Done'%i)

f2.close()
