N, L = map(int, input().split())
S = [input() for i in range(N)]
sort = sorted(S)

print(''.join(sort))
