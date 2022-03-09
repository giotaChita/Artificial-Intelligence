# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time

import numpy as np

def newtonF(x,a,b,c):
    x=x-(3*a*x*x+2*b*x+c)/(6*a*x+2*b)
    return x

def newtonG(x,a,b):
    at=a.transpose()
    aa=a+at
    inv=np.linalg.inv(aa)
    x=-np.matmul(inv,b)
    return x
def gradF(x,a,b,c,learn_rate = 0.168):
    dk = - (3*a*x*x +2*b*x + c)
    x_new = x + learn_rate * dk
    return x_new

def gradG(x,a,b,learn_rate=0.168):
    at = a.transpose()
    aa = a + at
    inv = np.linalg.inv(aa)
    dk = -(b+np.matmul(aa, x))
    x_new = x + learn_rate * dk
    return x_new


def funG(x,a,b,c):
    temp=np.matmul(x.transpose(),a)
    xax=np.matmul(temp,x)
    bx=np.matmul(b.transpose(),x)
    ans=c+bx+xax
    return ans

type = input('Choose function type (1 for F(x), 2 for G(x)): ')
meth = input('Choose function minimalising method (1 for Gradient Descent, 2 for Newtons method): ')
bare = input('Do you want batch/restart mode? (1 for yes, 0 for no): ')
n=1
if(bare=='1'):
    n=input('How many times to do the operation? ')
    n=int(n)
defi = input('Choose the way of definition of starting points (1 for directly, 2 from Uniform Distribution): ')
low=0
high=0
if(defi=='2'):
    low,high=input('Define the range (give two numbers: low high): ').split()
    low=int(low)
    high=int(high)
stco = input('Choose the stopping condition (1 for number of iterations, 2 for desired value, 3 for computational time): ')
if(stco=='1'):
    t=input('Declare the number of iterations: ')
    t=int(t)

if (meth == '1'):
    if (type == '1'):
        (a, b, c, d) = input('declare the values of a, b, c and d: ').split()
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        ans = []
        while (n > 0):
            n = n - 1
            x = random.uniform(low, high)
            if (defi == '1'):
                x = input('Give starting (integer) point: ')
                x = int(x)
            if (stco == '1'):
                tt = t
                while (tt > 0):
                    tt = tt - 1
                    x = gradF(x, a, b, c)
            if (stco == '2'):
                dv = input('Give desired value: ')
                dv = int(dv);
                while ((a * pow(x, 3) + b * x * x + c * x + d) > dv):
                    x = gradF(x, a, b, c)
            if (stco == '3'):
                ct = input('Give computational time (in seconds): ')
                ct = int(ct)
                starttime = time.perf_counter()
                while (time.perf_counter() - starttime < ct):
                    x = gradF(x, a, b, c)

            ans.append(x)

        if (len(ans) == 1):
            x = ans[0]
            val = a * pow(x, 3) + b * x * x + c * x + d
            print(x, val)
        else:
            m = np.mean(ans)
            std = np.std(ans)
            print(m, std)

    elif (type == '2'):
        c = input('Enter value c: ')
        c = int(c)
        b = list(map(int, input("Enter d-dimensional vector b: ").split()))
        d = len(b)
        b = np.array(b)
        a = [[0 for i in range(d)] for j in range(d)]
        i = 0
        print('Enter matrix A: ')
        while (i < d):
            a[i] = list(map(int, input().split()))
            i = i + 1
        a = np.array(a)
        ans = []
        while (n > 0):
            n = n - 1
            x = []
            for i in range(d):
                x.append(random.uniform(low, high))
            x = np.array(x)
            if (defi == '1'):
                x = list(map(int, input("Give starting point: ").split()))
                x = np.array(x)
            if (stco == '1'):
                tt = t
                while (tt > 0):
                    tt = tt - 1
                    x = gradG(x, a, b)
            if (stco == '2'):
                dv = input('Give desired value: ')
                dv = int(dv)
                while (funG(x, a, b, c) > dv):
                    x = gradG(x, a, b)
            if (stco == '3'):
                ct = input('Give computational time (in seconds): ')
                ct = int(ct)
                starttime = time.perf_counter()
                while (time.perf_counter() - starttime < ct):
                    x = gradG(x, a, b)

            ans.append(x)

        if (len(ans) == 1):
            x = ans[0]
            val = funG(x, a, b, c)
            print(x, val)
 
        else:
            ans = np.array(ans)
            m = np.mean(ans, axis=0)
            std = np.std(ans, axis=0)
            print(m, std)




if(meth=='2'):
    if(type=='1'):
        (a, b, c,d)=input('declare the values of a, b, c and d: ').split()
        a=int(a)
        b=int(b)
        c=int(c)
        d=int(d)
        ans=[]
        while(n>0):
            n=n-1
            x=random.uniform(low,high)
            if(defi=='1'):
                x=input('Give starting point: ')
                x=int(x)
            if(stco=='1'):
                tt=t
                while(tt>0):
                    tt=tt-1
                    x=newtonF(x,a,b,c)
            if(stco=='2'):
                dv=input('Give desired value: ')
                dv=int(dv);
                while((a*pow(x,3)+b*x*x+c*x+d)>dv):
                    x=newtonF(x,a,b,c)
            if(stco=='3'):
                ct=input('Give computational time (in seconds): ')
                ct=int(ct)
                starttime=time.perf_counter()
                while(time.perf_counter()-starttime<ct):
                    x=newtonF(x,a,b,c)

            ans.append(x)

        if(len(ans)==1):
            x=ans[0]
            val=a*pow(x,3)+b*x*x+c*x+d
            print(x,val)
        else:
            m=np.mean(ans)
            std=np.std(ans)
            print(m,std)

    elif (type == '2'):
        c = input('Enter value c: ')
        c=int(c)
        b = list(map(int, input("Enter d-dimensional vector b: ").split()))
        d=len(b)
        b=np.array(b)
        a=[[0 for i in range(d)] for j in range(d)]
        i=0
        print('Enter matrix A: ')
        while(i<d):
            a[i]=list(map(int, input().split()))
            i=i+1
        a=np.array(a)
        ans = []
        while (n > 0):
            n = n - 1
            x=[]
            for i in range(d):
                x.append(random.uniform(low,high))
            x=np.array(x)
            if (defi == '1'):
                x = list(map(int, input("Give starting point: ").split()))
                x=np.array(x)
            if (stco == '1'):
                tt=t
                while (tt > 0):
                    tt = tt - 1
                    x = newtonG(x, a, b)
            if (stco == '2'):
                dv = input('Give desired value: ')
                dv = int(dv);
                while (funG(x,a,b,c) > dv):
                    x = newtonG(x, a, b)
            if (stco == '3'):
                ct = input('Give computational time (in seconds): ')
                ct = int(ct)
                starttime = time.perf_counter()
                while (time.perf_counter() - starttime < ct):
                    x = newtonG(x, a, b)

            ans.append(x)

        if (len(ans) == 1):
            x = ans[0]
            val = funG(x,a,b,c)
            print(x, val)

        else:
            ans=np.array(ans)
            m = np.mean(ans,axis=0)
            std = np.std(ans,axis=0)
            print(m, std)
'''
            fig,ax = plt.subplots(figsize = (12, 8))
            ax.set_ylabel('x*')
            ax.set_xlabel('iterations')
            _ = ax.plot(ans, range(len(arr)),'b')
'''
