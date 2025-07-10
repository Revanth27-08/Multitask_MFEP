import numpy as np

unfolded_cut = -5
folded_cut = 5

stride=20

f2 = open('ts_data/all_data', 'w')

for i in range(1,11):#check
    f1 = open('ts_data/data_%d'%i,'w')
    l = np.loadtxt('run%d/COLVAR'%i)
    ll = np.loadtxt('run%d/COLVAR_descriptor'%i)
    
    l_flipped = np.flip(l,axis=0)[::stride]
    ll_flipped = np.flip(ll,axis=0)[::stride]
    
    #exclude portions beyond the unfolded cut and folded cut
    for j in range(len(l_flipped)):
        
        if l_flipped[j,2] < folded_cut and l_flipped[j,2] > unfolded_cut:
            for k in range(len(ll_flipped[j])):
                print(ll_flipped[j,k],end=' ',file=f1)
                print(ll_flipped[j,k],end=' ',file=f2)
            print(file=f1)
            
            print(file=f2)
            
        if l_flipped[j,2] >= folded_cut:
            break

    f1.close()
    print('traj_%d Done'%i)

f2.close()

