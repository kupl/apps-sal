(N,M) = map(int,input().split(' '))
S = []
for i in range(N+M):
    x = int(input())
    if x != -1:
        S.append(x)
    else:
        n = max(S)
        print(n)
        S.remove(n)
