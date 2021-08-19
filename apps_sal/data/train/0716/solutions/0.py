import math
n = 1001
a = [True] * n
l = []
for i in range(2, 33):
    if a[i]:
        for j in range(i * i, n, i):
            a[j] = False
for pr in range(2, 1001):
    if a[pr]:
        l.append(pr)
t = int(input())
for j in range(t):
    (n, m) = list(map(int, input().strip().split()))
    arr = [int(num) for num in input().strip().split()]
    Matrix = []
    index = [0] * 100000
    factors = [0] * 100000
    ans = ''
    for r in range(len(arr)):
        li = []
        for val in l:
            while arr[r] % val == 0:
                arr[r] = arr[r] / val
                li.append(val)
                factors[r] += 1
        if arr[r] != 1:
            li.append(arr[r])
            arr[r] = 1
            factors[r] += 1
        Matrix.append(li)
    for k in range(m):
        opr = [int(o) for o in input().strip().split()]
        L = opr[1]
        R = opr[2]
        if opr[0] == 0:
            for ran in range(L - 1, R):
                if index[ran] < factors[ran]:
                    index[ran] += 1
        else:
            result = 1
            for ran in range(L - 1, R):
                if index[ran] < factors[ran]:
                    result = max(result, Matrix[ran][index[ran]])
            ans += str(result)
            ans += ' '
    print(ans[:-1])
