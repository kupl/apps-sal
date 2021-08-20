(N, L) = map(int, input().split())
S = []
for n in range(N):
    s = input()
    S.append(s)
S.sort()
print(''.join(S))
