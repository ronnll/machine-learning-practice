import math
import sys

featureFile = sys.argv[1]
labelFile = sys.argv[2]
#featureFile = 
#labelFile = 

def getFeatureData(featureFile):
    x = []
    dFile = open(featureFile, 'r')
    for line in dFile:
        row = line.split()
        rVec = [float(item) for item in row]
        rVec.append(1)
        x.append(rVec)
    dFile.close()
    return x

def getLabelData(labelFile):
    lFile = open(labelFile, 'r')
    lDict = {}
    for line in lFile:
        row = line.split()
        if int(row[0]) == 0:
            lDict[int(row[1])] = -1
        else:
            lDict[int(row[1])] = int(row[0])
    lFile.close()
    return lDict

featureData = getFeatureData(featureFile)
labelData = getLabelData(labelFile)
column = len(featureData[0])
row = len(featureData)

def dotpro(w, w0):
    return sum([w[i] * w0[i] for i in range(0, column, 1)])

w = []
for i in range(0, column, 1):
    w.append(0.01)

eta = 0.0001
stop = 0.000000001
repeat = 1
norm = 0

while 1==1:
    alpha = []
    for i in range(0, column, 1):
        alpha.append(0)
    loss = 0
    for p in range(0, row, 1):
        if labelData.get(p) is not None:
            dotproduct = dotpro(w, featureData[p])
            if((dotproduct < 0 and labelData.get(i) > 0) or (dotproduct > 0 and labelData.get(i) < 0)):
                for l in range(0, column, 1):
                    alpha[l] += -1 * (featureData[p][l] * labelData.get(p))
                    loss += max(0, 1 - dotproduct)

    print("The loss is: ", loss)
    if loss == 0:
        break
    for i in range(0, column, 1):
        w[i] = w[i] - eta * alpha[i]
    repeat += 1

for i in range(0, (column - 1), 1):
    norm += w[i] ** 2
	
print("The w is: ", w)
norm = math.sqrt(norm)
origin = abs(w[len(w) - 1] / norm)
print("The length of Distance is = " + str(origin))

for i in range(0, row, 1):
    if (labelData.get(i) is None):
        dotproduct = dotpro(w, featureData[i])
        if (dotproduct > 0):
            print("1 " + str(i))
        else:
            print("0 " + str(i))
