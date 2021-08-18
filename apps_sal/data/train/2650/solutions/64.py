N, L = list(map(int, input().split()))
S = []
for i in range(N):
    S.append(input())
S.sort()
result = ""
for i in range(N):
    result = result + S[i]
print(result)
