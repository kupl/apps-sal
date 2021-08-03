from bisect import bisect_right
s = list(map(int, list(input())))
s.insert(0, -1)
n = len(s) - 1
flag = 0
if s[n] == 1 or s[1] == 0 or s[n - 1] == 0:
    flag = 1
else:
    for i in range(2, n - 1):
        if s[i] != s[n - i]:
            flag = 1
            break
if flag == 1:
    print(-1)
else:
    print(n, n - 1)
    A = [1, n - 1]
    cur = 1
    for i in range(2, n - 1):
        if s[i] == 1:
            print(cur, i)
            cur = i
            A.append(i)
    print(cur, n - 1)
    A = sorted(A)
    for i in range(2, n - 1):
        if s[i] == 0:
            ind = bisect_right(A, i)
            print(i, A[ind])
