import math
from Components.Cost import Cost

def sigmoid(z):
    g = [[0 for col in range(len(z[0]))] for row in range(len(z))]
    for i in range(len(z)):
        for j in range(len(z[0])):
            g[i][j] = 1/(1 + math.exp(-z[i][j]))
    return g

def LogRegCostReg(theta, X, y, la):
    m = len(y)
    J = 0
    grad = [0 for _ in range(len(theta))]
    for i in range(m):
        h = 0
        for j in range(len(theta)):
            h += X[i][j] * theta[j]
        h = sigmoid(h)
        J = J - y[i] * math.log(h) - (1 - y[i]) * math.log(1 - h)
        for j in range(len(theta)):
            grad[j] = grad[j] + (h - y[i]) * X[i][j]
    J = J/m + la/(2 * m) * [ x**2 for x in theta[1:len(theta)-1]]
    grad[0] = grad[0]/m
    for i in range(1,len(grad)):
        grad[i] = (grad[i] + la * theta(i))/m

    return Cost(J, grad)

def LogRegCost(theta, X, y):
    return LogRegCostReg(theta, X, y, 0)