

def matMult(A, B):
    if len(A[0]) != len(B):
        print("Dimensions must agree. Returning...")
        return []

    aRows = len(A)
    bCols = len(B[0])
    aCols = len(A[0])
    out = [[0 for i in range(bCols)] for j in range(aRows)]

    for i in range(aRows):
        for j in range(bCols):
            for k in range(aCols):
                out[i][j] += A[i][k] * B[k][j]
    return out

A  = [[1, 2, 3], [4, 5, 6]]
B = [[1, 4], [2, 5], [3, 6]]
print(matMult(A,B))