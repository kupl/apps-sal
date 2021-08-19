N = int(input())
B = list(map(int, input().split()))
A = [(B[i], i) for i in range(N)]
A.sort(key=lambda x: x[0], reverse=True)
A.append((0, 0))
ans = [0] * N
tmp = N + 1
count = 1
for (index, a) in enumerate(A[:-1]):
    tmp = min(tmp, a[1])
    ans[tmp] += count * (a[0] - A[index + 1][0])
    count += 1
print(*ans, sep='\n')
