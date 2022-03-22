import numpy as np
import random


# Transform our elements from binary to decimal (using the first bit to define the sign of the number

def ma2vec(m, d):
    x = []
    for i in range(d):
        t = 0
        tt = 0
        if m[i][0] == 0:
            for j in range(d):
                if tt == 0:
                    tt = 1
                    continue
                t *= 2
                t += j
        else:
            for j in m[i]:
                if tt == 0:
                    tt = 1
                    continue
                t *= 2
                t += j
            t = -t
        x.append(t)
    x = np.array(x)
    return x


# function f(x) = x^TAx + b^Tx + c
def func(a, b, c, po, d):
    x = ma2vec(po, d)
    temp = np.matmul(x.transpose(), a)
    xax = np.matmul(temp, x)
    bx = np.matmul(b.transpose(), x)
    ans = c + bx + xax
    return ans


def user_inputs():
    dim = input('Give function dimensionality: ');
    dim = int(dim)
    print('Give matrix A (each row you add press Enter) : ')
    a = [[0 for i in range(dim)] for j in range(dim)]
    i = 0
    while i < dim:
        a[i] = list(map(int, input().split()))
        i += 1
    a = np.array(a)
    b = list(map(int, input("Give d-dimensional vector b: ").split()));
    b = np.array(b)
    c = input('Give constant c: ');
    c = int(c)
    d = int(input('Give the range of searched integers as 𝑑≥1 that for each dimension i, −2^d<xi<2^d: '))
    psize = int(input('Give population size: '));
    pairs = psize // 2
    pcr = float(input('Give crossover probability: '))
    while pcr < 0 or pcr > 1:
        pcr = float(input('Give another crossover probability (in range (0,1)) : '))
    pmu = float(input('Give mutation probability: '))
    while pmu < 0 or pmu > 1:
        pmu = float(input('Give another mutation probability (in range(0,1)): '))
    ite = int(input('Give number of iterations: '))
    repl = int(input('How many individuals to replace in each iteration? '))
    return dim, a, b, c, d, psize, pcr, pmu, ite, repl, pairs


def mutation(psize, pop):
    for i in range(psize):
        mut = np.random.binomial(size=1, n=1, p=pmu)
        if mut == 0:
            continue
        for k in range(dim):
            btm = random.randrange(1,
                                   d // 2)  # only last bits to mutate because the new number must be close to the old
            for j in range(btm):
                if np.random.binomial(size=1, n=1, p=pmu) == 0:
                    continue
                pop[i][k][d - j] = (pop[i][k][d - j] + 1) % 2
    return pop


def crossover(pairs, pop):
    for i in range(pairs):
        cross = np.random.binomial(size=1, n=1, p=pcr)
        if cross == 0: continue
        par1 = pop[2 * i]
        par2 = pop[2 * i + 1]
        # sp is the random point where the crossover will be performed
        sp = random.randrange(d // 2, d + 1)
        child1 = []
        child2 = []

        # while
        # while -> choose if
        # k = random.randint(1,dim)

        for k in range(dim):
            child1.append(par1[k][:sp] + par2[k][sp:])
            child2.append(par2[k][:sp] + par1[k][sp:])
        pop[2 * i] = child1
        pop[2 * i + 1] = child2
    return pop


def genetic_algorithm(pop):
    val = []
    min = 0;
    max = 0
    for i in pop:
        t = func(a, b, c, i, dim)
        if len(val) == 0:
            min = t
            max = t
        elif t < min:
            min = t
        elif t > max:
            max = t
        val.append(t)
    print(np.mean(val))
    print(np.max(val))
    sum = 0
    for i in range(psize):
        val[i] = (val[i] - min) / (max - min)
        sum += val[i]
    # print(val)
    prob = []
    for i in range(psize):
        prob.append((val[i]) / sum)
    return pop


def roulette_wheel_selection(pop, val, repl, psize, offset):
    temp = random.choices(np.arange(0, psize), weights=(val), k=repl)
    tpop = []
    for i in range(repl):
        tpop.append(pop[temp[i]])

    for i in range(repl):
        pop[(i + offset) % psize] = tpop[i]
        offset = (offset + repl) % psize
    return pop


                    ### MAIN ###

# initialization
dim, a, b, c, d, psize, pcr, pmu, ite, repl, pairs = user_inputs()
fifo = 0
offset = 0
pop = [[[random.randint(0, 1) for i in range(d + 1)] for j in range(dim)] for k in range(psize)]
while ite > 0:
    ite -= 1
    pop, val = genetic_algorithm(pop)
    pop = roulette_wheel_selection(pop, val, repl, psize, offset)
    pop = crossover(pairs, pop)
    pop = mutation(psize, pop)
print('final population', pop)

