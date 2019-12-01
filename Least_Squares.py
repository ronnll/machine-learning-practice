#least square
import sys
import math
import random

def getFeatureData(featureFile):
    x=[]
    dFile = open(featureFile, 'r')
    for line in dFile:
        row = line.split()
        rVec = [float(item) for item in row]
        x.append(rVec)
    dFile.close()
    return x

def getLabelData(labelFile):
    lFile = open(labelFile, 'r')
    lDict = {}
    for line in lFile:
        row = line.split()
        lDict[int(row[1])] = int(row[0])
    lFile.close()
    return lDict

featurefile = getFeatureData(sys.arg[1])
labelFile = getLabelData(sys.arg[1])

def dopro(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])
C = len(featureData[0])
R = len(featureData)
eta = 0.001
a = []
for i in range(len(featureData[0])):
    a.append(random.uniform(-0.01, 0.01))
dist = 10 + R
disparity = 1
while ((disparity) > 0.00001):
    G = []
    for alpha in range(0, C, 1):
        G.append(0)
    for beta in range(0, R, 1):
        if (labelData.get(str(beta)) != None):
            dots = dopro(a, featureData[beta])
            for gamma in range(0, C, 1):
                G[gamma] += (labelData.get(str(beta)) - dots) * featureData[beta][gamma]
    for beta in range(0, C, 1):
        a[beta] = a[beta] + eta * G[beta]
        epsilon = dist
        dist = 0
        for beta in range(0, R, 1):
            if (labelData.get(str(beta)) != None):
                dist += (labelData.get(str(beta)) - dopro(a, featureData[beta])) ** 2
        if (epsilon > dist):
            disparity = epsilon - dist
        else:
            disparity = dist - epsilon
value = 0
for i in range(0, (C - 1), 1):
    value += a[i] ** 2
print (a)
value = math.sqrt(value)
from0 = abs(a[len(a) - 1] / value)
print (str(from0))
