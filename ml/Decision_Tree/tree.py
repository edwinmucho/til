from math import log

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCnt = {}

    for featvec in dataSet:
        curlab = featvec[-1]
        if curlab not in labelCnt.keys():
            labelCnt[curlab] = 0
        labelCnt[curlab] += 1
    shannonEnt = 0
    for k in labelCnt.values():
        prob = float(k) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        print("{}\n{}/{}/{}".format(featVec,featVec[:axis], featVec[axis], featVec[axis+1:]))
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


myData, labels = createDataSet()
print(myData)
print(labels)

c = calcShannonEnt(myData)
print(c)

s = splitDataSet(myData, 1, 1)
print(s)