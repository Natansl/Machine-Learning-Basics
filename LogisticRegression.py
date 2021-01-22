import math

def sigmoid(z):
    g = [[0 for col in range(len(z[0]))] for row in range(len(z))]
    for i in range(len(z)):
        for j in range(len(z[0])):
            g[i][j] = 1/(1 + math.exp(-z[i][j]))
    return g

def LogRegCost(theta, X, y):
    m = len(y)
    J = 0
    for i in range(m):
        h = 0
        for j in range(len(theta)):
            h += X[i][j] * theta[j]
        h = sigmoid(h)
        J = J - y[i] * math.log(h) - (1 - y[i]) * math.log(1 - h)
    J /= m
    return J