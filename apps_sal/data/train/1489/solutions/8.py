N, K = input().split()
N, K = list(N), int(K)

for i in range(len(N)):
    if K and N[i] != '9':
        N[i] = '9'
        K -= 1
print(''.join(N))
