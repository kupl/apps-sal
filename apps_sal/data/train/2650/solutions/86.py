
N, L = list(map(int, input().split()))
S = []
for i in range(N):
    S.append(input())
S.sort()
out = ''
for i in range(N):
    out = out + S[i]

print(out)
