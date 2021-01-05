           ##Finite element analysis -Bar and truss##

import numpy as np
##input of material properties and no of nodes are considered in object to prepare model##
N= int(input("enter the total number of nodes :"))
E =[]
l =[]
A =[]
for x in range(N -1) :
     E.append(int(input("Elastic modulas (N/mm2) of %d element:" %x)))
     l.append(int(input("length (mm) of %d element:" %x)))
     A.append(int(input("Cross section (mm2) of %d element:" %x)))

##Element lavel stifness matrix##          
x=[]  
j= 0
k=0
r=0
my_E = np.asarray(E)
my_l = np.asarray(l)
my_A = np.asarray(A)

for j in my_E: 
    for k in my_l:
        for r in my_A:
            c = j*r/k  # formula of linear stifness 
    x.append(c)

arr2 = np.array([[1, -1], [-1 ,1]])   #unit matrix
V=[]
for i in x:
    v=i*arr2    #element matrix
    V.append(v)
for i in range(len(V)):
    print("element stifness matrix of",i,":",V[i])

#####Global stifness Matrix####inprogress#####
G_Mat = [ [ 0 for i in range(N) ] for j in range(N) ] 





      





