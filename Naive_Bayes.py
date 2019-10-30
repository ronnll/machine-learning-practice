#Ronny Lim _ Assignment 1 _ CS675 Fall2018#
import math
import sys

featureFile = sys.argv[1]
labelFile = sys.argv[2]

def getFeatureData(featureFile):
    x=[]
    dFile = open(featureFile, 'r')
    for line in dFile:
        row = line.split()
        rVec = [float(each) for each in row]
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
DataA = getFeatureData(featureFile)
DataB = getLabelData(labelFile)
without_0 = []
with_1 = []
for each in DataB:
    if DataB[each] == 0:
        with_1.append(DataA[each])
    elif DataB[each] == 1:
        with_1.append(DataA[each])
def averages(ListA):
    return sum(ListA)/len(ListA)
def StanDev(ListA):
    mean = averages(ListA)
    sum = 0
    for each in ListA:
        x = (each - mean)**2
        sum = sum + x
    vari = sum/len(ListA)
    return math.sqrt(vari)
def StanDev2(ListB):
    ArrayA = []
    for i in range(len(ListB[0])):
        ListA = []
        for each in ListB:
            ListA.append(each[i])
        mean = averages(ListA)
        stddev = StanDev(ListA)
        ArrayA.append([mean,stddev])
    return ArrayA
classtype0 = StanDev2(without_0)
classtype1 = StanDev2(with_1)
testListB = {}
for EachC, data in enumerate(DataA):
    if EachC not in DataB:
        testListB[EachC] = data
assum ={}
for EachD in testListB:
    total0 = 0
    total1 = 0
    each = testListB[EachD]
    for EachE, gett in enumerate(each):
        Matrix0 = classtype0[EachE][0]
        Pr0 = classtype0[EachE][1]
        zeta = 0
        if Pr0 != 0:
            zeta = pow((gett - Matrix0)/Pr0, 2)
        total0 = total0 + zeta
        Matrix1 = classtype1[EachE][0]
        Pro1 = classtype1[EachE][1]
        iota = 0
        if Pro1 != 0:
            iota = pow((gett - Matrix1)/Pro1, 2)
        total1 = total1 + iota
    if(total0 < total1):
        assum[EachD] = 0
    elif(total1 < total0):
        assum[EachD] = 1	
for EachF, EachG in assum.items():
    print(EachG, EachF)
ultdata = getLabelData(featureFile.replace('.data','.labels'))
Accur = 0
for i in assum:
    if assum[i] == ultdata[i]:
        Accur += 1
accuracy = Accur*100/len(assum)
print('The accuracy is ', accuracy)