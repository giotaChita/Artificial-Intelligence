import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import tree
import time

with open('kddcup.data.corrected', 'rb') as f:
    inputs = f.readlines()

packets = []
for item in inputs:
    packets.append(str(item)[2:(len(item)+1)])

hX = []
hy = []
for packet in packets:
    strlistpac = packet.split(",")
    take = np.random.binomial(1, 0.01)
    if take == 0:
        continue
    if "normal" in packet:
        hy.append(0)
    else:
        hy.append(1)
    hX.append([float(x)for x in strlistpac[4:41]])

# hyperparameter optimization
hX = list(map(list, zip(*hX)))
bestparam = []
bestcla = 0
method = int(input("Enter method : 1 for SVM and 2 for Decision Tree:\n"))
start = time.time()
for i in range(100):
    param = random.sample(range(0,37),10)
    htX = []
    for z in param:
        htX.append(hX[z])
    htX = list(map(list, zip(*htX)))
    xtrain, xtest, ytrain, ytest = train_test_split(htX, hy, test_size=0.3, random_state=32)
    if method == 1:
        model = SVC()
    elif method == 2:
        model = tree.DecisionTreeClassifier()
    model.fit(xtrain, ytrain)
    cla = model.score(xtest, ytest)
    if bestcla < cla:
        bestcla = cla
        bestparam = param.copy()

htX = []
for z in bestparam:
    htX.append(hX[z])
htX = list(map(list, zip(*htX)))
if method == 1:
    model = SVC()
elif method == 2:
    model = tree.DecisionTreeClassifier()
model.fit(htX, hy)

with open('corrected', 'rb') as f:
    inputs = f.readlines()

packets = []
for item in inputs:
    packets.append(str(item)[2:(len(item)+1)])

X = []
y = []
for packet in packets:
    strlistpac = packet.split(",")

    if "normal" in packet:
        y.append(0)
    else:
        y.append(1)
    X.append([float(x)for x in strlistpac[4:41]])

X = list(map(list, zip(*X)))
htX = []
for z in bestparam:
    htX.append(X[z])
X = list(map(list, zip(*htX)))
print("The packets are correctly classified with probability:\n", model.score(X,y))
end = time.time()
print("Computational time : \n", end-start)
