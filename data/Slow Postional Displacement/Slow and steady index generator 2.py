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
step_total = 60
step_disp = step_total/2
step_size = acc_max/(step_total/2)
dwell = 1000

relpos = list(np.append(np.linspace(step_size,acc_max,step_disp),np.linspace(acc_max-step_size,acc_min,step_disp)))
steps = np.append([step_size],np.diff(relpos))
indices=np.linspace(0,step_total-1,step_total)
plotindices=np.linspace(-1,step_total-1,step_total+1)

plt.figure()
plt.plot(indices,steps)
path=plt.figure()
plt.plot(plotindices,np.append([0],100*np.array(relpos)/acc_max))
plt.xlabel("command index")
plt.ylabel(r"roller position %")

outputfile=''

for i , step in enumerate(steps):
    step=int(step)
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
        outputfile+='Dwell Time,'+str(dwell)+'\n'
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

setnum=str(dwell)+' ms'
with open("set "+setnum+" dwell indexes for ramp and return drop bear "+str(step_total)+" steps.txt",'w') as f:
    f.write(outputfile)
plt.savefig("set "+setnum+" commanded motion.png",dpi=300)






#A = np.ones((5,5))
#B = np.ones((5,5))
##A[2,2] = 0
#
#
#
#C = np.matmul(A,B)

















































