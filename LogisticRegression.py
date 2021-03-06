import math
import MathOperators
from Components import CostOut

def sigmoid(z):
    g = [[0 for col in range(len(z[0]))] for row in range(len(z))]
    for i in range(len(z)):
        for j in range(len(z[0])):
            g[i][j] = 1/(1 + math.exp(-z[i][j]))
    return g

def oneVAll(X, allTheta):
    m = len(X)
    num_param = len(allTheta)
    p = []
    for i in range(m):
        pred = [sigmoid(MathOperators.matMult(allTheta[j], MathOperators.transpose(X[i]))) for j in range(num_param)]
        p.append(pred.index(max(pred)) + 1)
    return p    


def LogRegCostReg(theta, X, y, la):
    m = len(y)
    J = 0
    grad = [0 for _ in range(len(theta))]
    for i in range(m):
        h = sigmoid(MathOperators.matMult(X[i], MathOperators.transpose(theta)))
        J = J - y[i] * math.log(h) - (1 - y[i]) * math.log(1 - h)
        for j in range(len(theta)):
            grad[j] = grad[j] + (h - y[i]) * X[i][j]
    J = J/m + la/(2 * m) * [ x**2 for x in theta[1:len(theta)-1]]
    grad[0] = grad[0]/m
    for i in range(1,len(grad)):
        grad[i] = (grad[i] + la * theta(i))/m

    return CostOut(J, grad)

def LogRegCost(theta, X, y):
    return LogRegCostReg(theta, X, y, 0)