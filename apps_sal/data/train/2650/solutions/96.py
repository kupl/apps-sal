N,L=map(int, input().split())
S=[]

for i in range(N):
    S.append(input())
S.sort()

for i in range(N):
    print(S[i], end="")
