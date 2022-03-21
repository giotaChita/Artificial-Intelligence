#Exercise 2

import numpy as np
import random


def ma2vec(m,d):
    x=[]
    for i in range(d):
        if m[i][0]==0:
            t=0
            tt=0
            for j in m[i]:
                if tt==0:
                    tt=1
                    continue
                t=t*2
                t=t+j
        else:
            t = 0
            tt = 0
            for j in m[i]:
                if tt == 0:
                    tt = 1
                    continue
                t = t * 2
                #t = t + (j+1)%2
                t=t+j
            #t=t+1
            t=-t
        x.append(t)
    x=np.array(x)
    return x


def fun(a,b,c,po,d):
    x=ma2vec(po,d)
    temp = np.matmul(x.transpose(), a)
    xax = np.matmul(temp, x)
    bx = np.matmul(b.transpose(), x)
    ans = c + bx + xax
    return ans


dim = input('Give function dimensionality: ')
dim=int(dim)
print('Give matrix A (each row you add press Enter) : ')
a = [[0 for i in range(dim)] for j in range(dim)]
i=0
while i < dim:
    a[i] = list(map(int, input().split()))
    i = i + 1
a = np.array(a)
b = list(map(int, input("Give d-dimensional vector b: ").split()))
b = np.array(b)
c = input('Give constant c: ')
c=int(c)
d = int(input('Give the range of searched integers as 𝑑≥1 that for each dimension i, −2^d<xi<2^d: '))
psize= int(input('Give population size: '))
pairs=psize//2
pcr= float(input('Give crossover probability: '))
pmu= float(input('Give mutation probability: '))
ite=int(input('Give number of iterations: '))
repl=int(input('How many individuals to replace in each iteration? '))
offset=0
pop=[[[random.randint(0,1) for i in range(d+1)]for j in range(dim)]for k in range(psize)]
#print(pop)

fifo=0

while(ite>0):
    ite=ite-1
    val=[]
    min=0
    max=0
    for i in pop:
        t=fun(a,b,c,i,dim)
        if len(val)==0:
            min=t
            max=t
        elif t<min:
            min=t
        elif t>max:
            max=t
        val.append(t)
    #print(val)
    print(np.mean(val))
    print(np.max(val))
    sum=0
    for i in range(psize):
        val[i]=(val[i]-min)/(max-min)
        sum=sum+val[i]
    #print(val)
    prob=[]
    for i in range(psize):
        prob.append((val[i])/sum)
    #print(prob)

    temp=random.choices(np.arange(0,psize), weights=(val) , k=repl)
    #print(temp)

    tpop=[]
    for i in range(repl):
        tpop.append(pop[temp[i]])
    #print(tpop)

    for i in range(repl):
        pop[(i+offset)%psize]=tpop[i]
        offset=(offset+repl)%psize
    #print(pop)

    for i in range(pairs):
        cross=np.random.binomial(size=1, n=1, p=pcr)
        if cross==0: continue
        par1=pop[2*i]
        par2=pop[2*i+1]
        sp=random.randrange(d//2,d+1)
        child1=[]
        child2=[]
        #while -> choosediff
        for k in range(dim):
            child1.append(par1[k][:sp]+par2[k][sp:])
            child2.append(par2[k][:sp]+par1[k][sp:])
        pop[2*i]=child1
        pop[2*i+1]=child2

    #print(pop)

    for i in range(psize):
        mut = np.random.binomial(size=1, n=1, p=pmu)
        if(mut==0):
            continue
        for k in range(dim):
            btm=random.randrange(1,d//2)  #only last bits to mutate because the new number must be close to the old
            for j in range(btm):
                if np.random.binomial(size=1, n=1, p=pmu)==0:
                    continue
                pop[i][k][d-j]=(pop[i][k][d-j]+1)%2

    #print(pop)
