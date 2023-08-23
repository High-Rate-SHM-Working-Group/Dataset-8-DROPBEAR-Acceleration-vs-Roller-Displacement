# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
plt.close('all')

len_step = 20000
acc_max, acc_min = 60000, 0
accumulator = 0
steptotal = 32

relpos = []
steps = []
while len(steps) < steptotal-1:
    ustep = random.uniform(0.01,1.0)
    udir = random.choice([1,-1])
    len_step=random.choice([10000,30000,50000])
    nstep = int(udir*ustep*len_step)
    #print(nstep)
    naccumulator=accumulator+nstep
    if (naccumulator < acc_max)and(naccumulator >  acc_min):
        print(naccumulator)
        #print(udir)
        accumulator=naccumulator
        relpos.append(accumulator)
        steps.append(nstep) 
steps.append(-accumulator)
relpos.append(0)
indices=np.linspace(0,steptotal-1,steptotal)
plotindices=np.linspace(-1,steptotal-1,steptotal+1)

plt.figure()
plt.plot(indices,steps)
path=plt.figure()
plt.plot(plotindices,np.append([0],100*np.array(relpos)/acc_max))
plt.xlabel("command index")
plt.ylabel(r"roller position %")

outputfile=''

for i , step in enumerate(steps):
    if i+1==len(steps):
        outputfile+='[INDEX '+str(i)+']'+'\n'
        outputfile+='Index type,1'+'\n'
        outputfile+='Distance,'+str(step)+'\n'
        outputfile+='Velocity,2000000'+'\n'
        outputfile+='Acceleration,1500000'+'\n'
        outputfile+='Deceleration,1500000'+'\n'
        outputfile+='Reg. Distance,100000'+'\n'
        outputfile+='Reg. Velocity,1000000'+'\n'
        outputfile+='Repeat Count,1'+'\n'
        outputfile+='Dwell Time,0'+'\n'
        outputfile+='Next Index,'+str(i+1)+'\n'
        outputfile+='Action,0'+'\n'+'\n'
    else:
        outputfile+='[INDEX '+str(i)+']'+'\n'
        outputfile+='Index type,1'+'\n'
        outputfile+='Distance,'+str(step)+'\n'
        outputfile+='Velocity,2000000'+'\n'
        outputfile+='Acceleration,1500000'+'\n'
        outputfile+='Deceleration,1500000'+'\n'
        outputfile+='Reg. Distance,100000'+'\n'
        outputfile+='Reg. Velocity,1000000'+'\n'
        outputfile+='Repeat Count,1'+'\n'
        outputfile+='Dwell Time,'+str(int(random.uniform(50,500)))+'\n'
        outputfile+='Next Index,'+str(i+1)+'\n'
        outputfile+='Action,2'+'\n'+'\n'

while i < 64:
    outputfile+='[INDEX '+str(i)+']'+'\n'
    outputfile+='Index type,1'+'\n'
    outputfile+='Distance,'+str(0)+'\n'
    outputfile+='Velocity,2000000'+'\n'
    outputfile+='Acceleration,1500000'+'\n'
    outputfile+='Deceleration,1500000'+'\n'
    outputfile+='Reg. Distance,100000'+'\n'
    outputfile+='Reg. Velocity,1000000'+'\n'
    outputfile+='Repeat Count,1'+'\n'
    outputfile+='Dwell Time,0'+'\n'
    outputfile+='Next Index,'+str((i+1)%64)+'\n'
    outputfile+='Action,0'+'\n'+'\n'
    i+=1
    

print(outputfile)

setnum='9'
with open("set "+setnum+" random indexes for drop bear dwell varying.txt",'w') as f:
    f.write(outputfile)
plt.savefig("set "+setnum+" commanded motion dwell varying.png",dpi=300)






#A = np.ones((5,5))
#B = np.ones((5,5))
##A[2,2] = 0
#
#
#
#C = np.matmul(A,B)

















































