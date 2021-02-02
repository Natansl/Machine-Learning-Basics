

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

def transpose(A):
    if not isinstance(A[0], list):
        rows = 1
        cols = len(A)
    else:
        rows = len(A)
        cols = len(A[0])
        
    At = [[0 for i in range(rows)] for j in range(cols)]
    for i in range(rows):
        for j in range(cols):
            At[j][i] = A[i][j]
    return At

A  = [[1, 2, 3], [4, 5, 6]]
B = [[1], [2], [3]]
print(matMult(A,B))
print(transpose(A))