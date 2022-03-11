# exercise 1 : Applied Newton's and Gradient method on two functions F and G

# the user will input the needed data. NOTE: all the input data must be integers


import random
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def newton_f(x, a, b, c):
    x_new = x - (3 * a * x * x + 2 * b * x + c) / (6 * a * x + 2 * b)
    return x_new


def newton_g(x, a, b):
    # because G function is a quadrature function, strictly convex it has a unique minimum point
    # and the Newton's algorithm reaches the x* in one iteration.
    at = a.transpose()
    aa = a + at
    inv = np.linalg.inv(aa)
    x = -np.matmul(inv, b)
    return x


def gradient_f(x, a, b, c, learn_rate=0.168):
    dk = - (3 * a * x * x + 2 * b * x + c)
    x_new = x + learn_rate * dk
    return x_new


def gradient_g(x, a, b, learn_rate=0.168):
    at = a.transpose()
    aa = a + at
    inv = np.linalg.inv(aa)
    dk = -(b + np.matmul(aa, x))
    x_new = x + learn_rate * dk
    return x_new


def fun_g(x, a, b, c):
    temp = np.matmul(x.transpose(), a)
    xax = np.matmul(temp, x)
    bx = np.matmul(b.transpose(), x)
    ans = c + bx + xax
    return ans


def plot_f(a, b, c, d, xmin):
    x = np.linspace(-5, 5, 100)
    y = a * x ** 3 + b * x ** 2 + c * x + d
    ymin = []
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x, y, 'r')
    for i in range(len(xmin)):
        ymin.append(a * xmin[i] ** 3 + b * xmin[i] ** 2 + c * xmin[i] + d)
        plt.plot(xmin[i], ymin[i], 'bo')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title("F function and the x*")
    # show the plot
    plt.show()


type_func = input('Choose function type (1 for F(x), 2 for G(x)): ')
meth = input('Choose minimization method (1 for Gradient Descent, 2 for Newtons method): ')
bare = input('Do you want batch/restart mode? (1 for yes, 0 for no): ')
n = 1  # times for executing the program
if bare == '1':
    n = input('How many times to do the operation? ')
    n = int(n)
defi = input('Choose the way of definition of starting points (1 for directly, 2 from Uniform Distribution): ')
low = 0
high = 0
x_array = []

if defi == '2':
    low, high = input('Define the range (give two int numbers: low high): ').split()
    low = int(low)
    high = int(high)
stco = input(
    'Choose the stopping condition (1 for number of iterations, 2 for desired value, 3 for computational time): ')
if stco == '1':
    t = input('Declare the number of iterations: ')
    t = int(t)

if meth == '1':
    if type_func == '1':
        (a, b, c, d) = input('declare the values (integers) of a, b, c and d: ').split()
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        ans = []


        while n > 0:
            n = n - 1
            x = random.uniform(low, high)
            if defi == '1':
                x = input('Give starting (integer) point: ')
                x = int(x)
            if stco == '1':
                tt = t
                while tt > 0:
                    tt = tt - 1
                    x_array.append(x)
                    x = gradient_f(x, a, b, c)
                x_array.append(x)
                plt.figure(figsize=(8, 6))
                plt.scatter(range(len(x_array)), x_array, marker='o', color='red')
                plt.ylabel("x*")
                plt.xlabel("iterations")
                plt.title("Iterations-Xmin")
                plt.show()
                plot_f(a, b, c, d, x_array)
                x_array = []

            if stco == '2':
                dv = input('Give desired value: ')
                dv = int(dv)
                while (a * pow(x, 3) + b * x * x + c * x + d) > dv:
                    x_array.append(x)
                    x = gradient_f(x, a, b, c)
                x_array.append(x)
                plt.figure(figsize=(8, 6))
                plt.scatter(range(len(x_array)), x_array, marker='o', color='red')
                plt.ylabel("x*")
                plt.xlabel("iterations")
                plt.title("Iterations-Xmin")
                plt.show()
                plot_f(a, b, c, d, x_array)
                x_array = []
            if stco == '3':
                ct = input('Give computational time (in seconds): ')
                ct = int(ct)
                start_time = time.perf_counter()
                while (time.perf_counter() - start_time) < ct:
                    x_array.append(x)
                    x = gradient_f(x, a, b, c)
                x_array.append(x)
                x_array = []

            ans.append(x)

        if len(ans) == 1:
            x = ans[0]
            val = a * pow(x, 3) + b * x * x + c * x + d
            print("mean = ", x, " and the standard deviation = ", val)
        else:
            m = np.mean(ans)
            std = np.std(ans)
            print("mean = ", m, " and the standard deviation = ", std)

    elif type_func == '2':
        c = input('Enter value c: ')
        c = int(c)
        b = list(map(int, input("Enter d-dimensional vector b: ").split()))
        d = len(b)
        b = np.array(b)
        a = [[0 for i in range(d)] for j in range(d)]
        i = 0
        print('Enter matrix A (each row you add press Enter) : ')
        while i < d:
            a[i] = list(map(int, input().split()))
            i = i + 1
        a = np.array(a)
        ans = []
        while n > 0:
            n = n - 1
            x = []
            for i in range(d):
                x.append(random.uniform(low, high))
            x = np.array(x)
            if defi == '1':
                x = list(map(int, input("Give (integer) starting point: ").split()))
                x = np.array(x)
            if stco == '1':
                tt = t
                while tt > 0:
                    tt = tt - 1
                    x = gradient_g(x, a, b)
            if stco == '2':
                dv = input('Give desired value: ')
                dv = int(dv)
                while fun_g(x, a, b, c) > dv:
                    x = gradient_g(x, a, b)

            if stco == '3':
                ct = input('Give computational time (in seconds): ')
                ct = int(ct)
                start_time = time.perf_counter()
                while (time.perf_counter() - start_time) < ct:
                    x = gradient_g(x, a, b)

            ans.append(x)

        if len(ans) == 1:
            x = ans[0]
            val = fun_g(x, a, b, c)
            print(x, val)
        else:
            ans = np.array(ans)
            m = np.mean(ans, axis=0)
            std = np.std(ans, axis=0)
            print("mean = ", m, " and the standard deviation = ", std)

if meth == '2':
    if type_func == '1':
        (a, b, c, d) = input('declare the (int) values of a, b, c and d: ').split()
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        ans = []

        while n > 0:
            n = n - 1
            x = random.uniform(low, high)
            if defi == '1':
                x = input('Give starting point: ')
                x = int(x)
            if stco == '1':
                tt = t
                while tt > 0:
                    tt = tt - 1
                    x_array.append(x)
                    x = newton_f(x, a, b, c)
                x_array.append(x)
                plt.figure(figsize=(8, 6))
                plt.scatter(range(len(x_array)), x_array, marker='o', color='red')
                plt.ylabel("x*")
                plt.xlabel("iterations")
                plt.title("Iterations-Xmin")
                plt.show()
                plot_f(a, b, c, d, x_array)
                x_array = []

            if stco == '2':
                dv = input('Give desired value: ')
                dv = int(dv);
                while (a * pow(x, 3) + b * x * x + c * x + d) > dv:
                    x_array.append(x)
                    x = newton_f(x, a, b, c)
                x_array.append(x)
                plt.figure(figsize=(8, 6))
                plt.scatter(range(len(x_array)), x_array, marker='o', color='red')
                plt.ylabel("x*")
                plt.xlabel("iterations")
                plt.title("Iterations-Xmin")
                plt.show()
                plot_f(a, b, c, d, x_array)
                x_array = []
            if stco == '3':
                ct = input('Give computational time (in seconds): ')
                ct = int(ct)
                start_time = time.perf_counter()

                while (time.perf_counter() - start_time) < ct:
                    x_array.append(x)
                    x = newton_f(x, a, b, c)
                x_array.append(x)
                x_array = []
            ans.append(x)

        if len(ans) == 1:
            x = ans[0]
            val = a * pow(x, 3) + b * x * x + c * x + d
            print("mean = ", x, " and the standard deviation = ", val)
        else:
            m = np.mean(ans)
            std = np.std(ans)
            print("mean = ", m, " and the standard deviation = ", std)

    elif type_func == '2':
        c = input('Enter value c: ')
        c = int(c)
        b = list(map(int, input("Enter d-dimensional vector b: ").split()))
        d = len(b)
        b = np.array(b)
        a = [[0 for i in range(d)] for j in range(d)]
        i = 0
        print('Enter matrix A: ')
        while i < d:
            a[i] = list(map(int, input().split()))
            i = i + 1
        a = np.array(a)
        ans = []
        while n > 0:
            n = n - 1
            x = []
            for i in range(d):
                x.append(random.uniform(low, high))
            x = np.array(x)
            if defi == '1':
                x = list(map(int, input("Give starting point: ").split()))
                x = np.array(x)
            if stco == '1':
                tt = t
                while tt > 0:
                    tt = tt - 1
                    x = newton_g(x, a, b)
            if stco == '2':
                dv = input('Give desired value: ')
                dv = int(dv);
                while fun_g(x, a, b, c) > dv:
                    x = newton_g(x, a, b)
            if stco == '3':
                ct = input('Give computational time (in seconds): ')
                ct = int(ct)
                start_time = time.perf_counter()
                while (time.perf_counter() - start_time) < ct:
                    x = newton_g(x, a, b)

            ans.append(x)

        if len(ans) == 1:
            x = ans[0]
            val = fun_g(x, a, b, c)
            print("mean = ", x, " and the standard deviation = ", val)
        else:
            ans = np.array(ans)
            m = np.mean(ans, axis=0)
            std = np.std(ans, axis=0)
            print("mean = ", m, " and the standard deviation = ", std)

exit()
