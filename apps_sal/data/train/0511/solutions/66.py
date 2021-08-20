N = int(input())
(*A,) = map(int, input().split())
total = 0
for i in range(N):
    total ^= A[i]
print(*[total ^ A[i] for i in range(N)])
