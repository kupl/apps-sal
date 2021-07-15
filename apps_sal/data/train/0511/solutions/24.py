N = int(input())
A = list(map(int, input().split()))
all_xor = 0
for a in A:
    all_xor ^= a

for i in range(N):
    ans = all_xor ^ A[i]
    print(ans, end=" ")
print()
