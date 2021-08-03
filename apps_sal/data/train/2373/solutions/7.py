A = [0 for x in range(400005)]
t = int(input())


def mymin(a, b):
    if(a < b):
        return a
    else:
        return b


def mymax(a, b):
    if(a > b):
        return a
    else:
        return b


for tests in range(t):
    [n, k] = input().split()
    n = int(n)
    k = int(k)
    B = input().split()
    for i in range(2, (2 * k) + 1):
        A[i] = 0
    n2 = int(n / 2)
    for i in range(n2):
        B[i] = int(B[i])
        B[n - 1 - i] = int(B[n - 1 - i])
        mi = mymin(B[i], B[n - 1 - i])
        ma = mymax(B[i], B[n - 1 - i])
        A[2] += 2
        A[mi + 1] -= 1
        A[mi + ma] -= 1
        if(mi + ma + 1 <= 2 * k):
            A[mi + ma + 1] += 1
        if(ma + k + 1 <= 2 * k):
            A[ma + k + 1] += 1
    ans = n
    for i in range(2, (2 * k) + 1):
        A[i] += A[i - 1]
        if(A[i] < ans):
            ans = A[i]
    print(ans)
