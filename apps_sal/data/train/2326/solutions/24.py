N = int(input())
A = list(map(int, input().split()))
B = sorted([(i, a) for (i, a) in enumerate(A)], key=lambda x: x[1])[::-1] + [(N, 0)]
d = [0] * N
m = N
for i in range(N):
    m = min(m, B[i][0])
    d[m] += (i + 1) * (B[i][1] - B[i + 1][1])
print(*d, sep='\n')
