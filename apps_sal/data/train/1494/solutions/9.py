n = int(input())
lis = []
for _ in range(n):
    size = int(input())
    lis.append(size)
lis.sort()
lis.reverse()
j = 1
val = [True for _ in range(n)]
i = 0
cnt = n
if n == 1:
    print(1)
elif lis[0] == lis[n - 1]:
    print(n)
else:
    while i < n and j < n:
        if val[i] != True:
            i += 1
            continue
        if val[j] != True:
            j += 1
            continue
        if lis[j] * 2 <= lis[i]:
            val[i] = False
            val[j] = False
            i += 1
            j += 1
            cnt -= 1
        else:
            j += 1
    print(cnt)
