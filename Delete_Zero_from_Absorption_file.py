'''
Created on 20150205

@author: QSong_pku
'''
import numpy as np 
import os
my_dir=raw_input("the path")
filename=os.listdir(my_dir)

for I in filename:
    if I[-4:]=='.txt' and I[-5]!='_' and os.path.getsize(os.path.join(my_dir,I))>10000:
        print my_dir+'\\'+I
        data=np.loadtxt(my_dir+'\\'+I,delimiter=',',dtype=float)
        print data.shape
        del data[:,data[0,:]==0]
        print  data.shape
        np.savetxt(my_dir+'\\'+I[:-4]+'_'+I[-4:],delimiter=',')
        os.remove(my_dir+'\\'+I)
        del data
        