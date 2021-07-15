def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        print('Number of A columns must equal number of B rows.')
        return
    C = [[0],
         [0],
         [0],
         [0],
         [0]]
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total
    return C

def invert_matrix(A, tol=None):
    n = len(A)
    AM = A
    I = [[1,0,0,0,0],
          [0,1,0,0,0],
          [0,0,1,0,0],
          [0,0,0,1,0],
          [0,0,0,0,1]]
    IM = [[1,0,0,0,0],
          [0,1,0,0,0],
          [0,0,1,0,0],
          [0,0,0,1,0],
          [0,0,0,0,1]]
    indices = list(range(n))
    for fd in range(n):
        fdScaler = 1.0 / AM[fd][fd]
        for j in range(n):
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        for i in indices[0:fd] + indices[fd+1:]: 
            crScaler = AM[i][fd]
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    return IM

mean = lambda x: sum(x)/len(x)

class Datamining:

    def __init__(self, train_set):
        A = []
        v = []
        for k in range(5):
            v.append( [mean([y * x**k for x,y in train_set])] )
            A.append( [mean([x**(j+k) for x,y in train_set]) for j in range(5)] )
        B = invert_matrix(A)
        self.coefs = matrix_multiply(B,v)

    def predict(self, x):
        return sum([ a[0] * x**i for i,a in enumerate(self.coefs)])

