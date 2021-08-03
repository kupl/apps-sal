N, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ans = []

mina = A.index(min(A))
maxb = B.index(max(B))

for i in range(M):
    ans.append('{} {}'.format(mina, i))

for i in range(N):
    if(mina != i):
        ans.append('{} {}'.format(i, maxb))

for i in ans:
    print(i)
