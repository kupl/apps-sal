def find_a(array, n):
    if n >= 0:
        if n < 4:
            return array[n]
        else:
            A = array[:]
            B = [0, 0, 0, 0]
            B[1] = 3 * A[1] - A[0] - A[2]
            B[2] = 3 * A[2] - A[1] - A[3]
            B[0] = 3 * B[1] - B[2] - A[1]
            B[3] = 3 * B[2] - B[1] - A[2]
            for i in range(n - 3):
                A.append("undefined")
                B.append("undefined")
            for i in range(4, len(A)):
                A[i] = 3 * A[i - 1] - A[i - 2] - B[i - 1]
                B[i] = 3 * B[i - 1] - B[i - 2] - A[i - 1]
            return A[-1]
    else:
        A = array[:]
        B = [0, 0, 0, 0]
        B[1] = 3 * A[1] - A[0] - A[2]
        B[2] = 3 * A[2] - A[1] - A[3]
        B[0] = 3 * B[1] - B[2] - A[1]
        B[3] = 3 * B[2] - B[1] - A[2]
        for i in range(-n):
            A = ["undefined"] + A
            B = ["undefined"] + B
        for i in range(-n-1, -1, -1):
            A[i] = 3 * A[i + 1] - A[i + 2] - B[i + 1]
            B[i] = 3 * B[i + 1] - B[i + 2] - A[i + 1]
        return A[0]
