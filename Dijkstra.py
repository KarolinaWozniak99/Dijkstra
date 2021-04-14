# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:54:56 2020

@author: LENOVO
"""

M=[[0,3,0,0,3,0],
   [0,0,1,0,0,0],
   [0,2,0,3,0,1],
   [0,3,0,0,0,0],
   [0,0,0,0,0,2],
   [0,0,0,1,0,0]]


def Min(Q,d):
    mini=Q[0]
    for i in Q:
        if(d[i]<d[mini]):
            mini=i
    return mini
            


S=[]
Q=[0,1,2,3,4,5]
n=len(Q)
SQ=[False]*n

d=[]
for i in range(0,n):
    d.append(float("inf"))
p=[-1]*n


v=0
d[v]=0
for i in range(0,n-1):
    u=Min(Q,d)
    
    Q.remove(u)
    SQ[u]=True
    for w in range(0,n):
        if(M[u][w]!=0):
            if(SQ[w]==False):
                
                if(d[w]>d[u]+M[u][w]):
                    d[w]=d[u]+M[u][w]
                    p[w]=u
            else:
                while(SQ[w]!=False):
                    w=w+1
                    
print("tablica poprzedników",p)
print("tablica kosztów dojscia",d)

print("koszt dojscia do wierzchołka 0",d[0])
print("koszt dojscia do wierzchołka 1",d[1])
print("koszt dojscia do wierzchołka 2",d[2])
print("koszt dojscia do wierzchołka 3",d[3])
print("koszt dojscia do wierzchołka 4",d[4])
print("koszt dojscia do wierzchołka 5",d[5])

                