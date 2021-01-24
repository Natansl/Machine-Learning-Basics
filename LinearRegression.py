import math

def LinRegCost(X, y, theta):
    dataSize = len(X)
    cost = 0
    for i in range(dataSize):
        Xi = 0
        for j in range(len(theta)):
            Xi += X[i][j] * theta[j]
        cost += pow((Xi-y(i)),2)
    cost /= 2 * dataSize
    return cost

def featureNormalize(X):
    mean = sum(X)/len(X)
    std = math.sqrt(sum((x - mean) ** 2 for x in X)/len(X))
    Xnorm = [(x - mean)/std for x in  X]
    return Xnorm