import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
data = loadmat('data_covid.mat',squeeze_me = True )
print(data.keys())
Z = data['Z']
# days = data['days']
print(type(Z))
print(Z.shape)
plt.figure(1)
plt.plot(Z)
# plt.show()


Z_t=[0,10,250]
p_t=range(0,400)

def d_kl(z,p):
    if z>0 and p>0:
        d=z*np.log(z/p)+p-z
        grad=1-(1/p)
    elif z==0 and p>=0:
        d=p
        grad=1
    else:
        d=np.inf 
        grad=np.inf  
        
    return d,grad    


    

plt.figure(2)
for i in Z_t:
    dK=[]
    g=[]
    for j in p_t:
        d,grad=d_kl(i,j)
        g.append(grad)
        dK.append(d) 
    # print('dk',dK) 
    print('g',g)   
    plt.plot(dK)
    
plt.show()        