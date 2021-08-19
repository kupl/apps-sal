N = int(input())
a = list(map(int, input().split()))
B = a[0]
for i in range(1, N):
    B ^= a[i]
print(' '.join([str(B ^ i) for i in a]))
