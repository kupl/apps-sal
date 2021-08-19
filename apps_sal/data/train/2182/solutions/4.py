from sys import stdin, stdout


def rint():
    return map(int, stdin.readline().split())


a = list(input())
b = list(input())
a.sort()
b.sort(reverse=True)
n = len(a)
ans = ['' for i in range(n)]
ai = 0
bi = 0
aj = 0
bj = 0
aiend = n // 2 - 1
if n % 2:
    aiend += 1
biend = n // 2 - 1
i = 0
j = 0
flag = 0
while i + j < n:
    if i + j < n:
        if a[ai] < b[bi] and flag == 0:
            ans[i] = a[ai]
            i += 1
            ai += 1
        else:
            ans[n - j - 1] = a[aiend - aj]
            j += 1
            aj += 1
            flag = 1
    if i + j < n:
        if a[ai] < b[bi] and flag == 0:
            ans[i] = b[bi]
            i += 1
            bi += 1
        else:
            ans[n - j - 1] = b[biend - bj]
            j += 1
            bj += 1
            flag = 1
print(''.join(ans))
