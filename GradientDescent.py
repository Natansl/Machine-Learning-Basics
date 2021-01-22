from LinearRegression import computeCost

def gradientDescent(X, y, theta, alpha, iter):
    m = len(X)
    for _ in range(iter):
        for i in range(len(theta)):
            nextTheta = []
            summ = 0
            for j in range(m):
                Xi = 0
                for z in range(len(theta)):
                    Xi += X[j][z] * theta[z]
                summ += X[j][i] * (Xi - y(j))
            nextTheta.append(theta(i) - alpha * summ / m)
        theta = nextTheta
    return theta