

def matMult(A, B):
    if not isinstance(A[0],list):
        aRows = 1
        aCols = len(A)
    else:
        aRows = len(A)
        aCols = len(A[0])
    
    if not isinstance(B[0],list):
        bRows = 1
        bCols = len(B)
    else:
        bRows = len(B)
        bCols = len(B[0])

    if aCols != bRows:
        print("Dimensions must agree. Returning...")
        return []

    out = [[0 for i in range(bCols)] for j in range(aRows)]

    for i in range(aRows):
        for j in range(bCols):
            for k in range(aCols):
                out[i][j] += A[i][k] * B[k][j]

    if len(out[0]) == 1 and len(out) == 1:
        out = out[0]
    return out

A  = [[1, 2, 3]]
B = [[1], [2], [3]]
print(matMult(A,B))