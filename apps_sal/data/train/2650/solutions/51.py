(N, L) = map(int, input().split())
S = []
for i in range(N):
    array = input()
    S.append(array)
S.sort()
S = ''.join(S)
print(S)
