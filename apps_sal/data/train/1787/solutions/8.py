def identity_matrix(n):
    """
    Creates and returns an identity matrix.
        :param n: the square size of the matrix
        :returns: a square identity matrix
    """
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = 1.0
    return I


def invert_matrix(A, tol=None):
    """
    Returns the inverse of the passed in matrix.
        :param A: The matrix to be inversed

        :return: The inverse of the matrix A
    """
    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)
    indices = list(range(n))
    for fd in range(n):
        fdScaler = 1.0 / AM[fd][fd]
        for j in range(n):
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        for i in indices[0:fd] + indices[fd + 1:]:
            crScaler = AM[i][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    return IM


def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)
    return A


def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])
    MC = zeros_matrix(rows, cols)
    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]
    return MC


def matrix_multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        print('Number of A columns must equal number of B rows.')
        return
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total
    return C


def transposeMatrix(m):
    return list(map(list, list(zip(*m))))


class Datamining:

    def __init__(self, train_set, n=6):
        self.data = train_set
        self.n = n
        self.m = len(self.data)
        self.fit()

    def fit(self):
        (X, ys) = ([], [])
        for (x, y) in self.data:
            X.append([x ** i for i in range(self.n)])
            ys.append([y])
        Xt = transposeMatrix(X)
        iv = invert_matrix(matrix_multiply(Xt, X))
        R = matrix_multiply(iv, Xt)
        self.weights = matrix_multiply(R, ys)

    def predict(self, x):
        xs = [[x ** i for i in range(self.n)]]
        return matrix_multiply(xs, self.weights)[0][0]
