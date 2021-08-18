N = int(input())
A = [0]
A += [int(x) for x in input().split()]
i = 0
while i <= N and i == A[i]:
    i += 1
j = N
while j >= i and j == A[j]:
    j -= 1
t = i
flg = True
for k in range(j, i - 1, -1):
    if A[k] != t:
        flg = False
        break
    t += 1
if i > j:
    flg = False
if flg:
    print(i, j)
else:
    print(0, 0)
