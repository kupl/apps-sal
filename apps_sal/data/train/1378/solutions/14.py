A, N, K = map(int, input().split())
R = [0]*K
i = 0

while A != 0 and i < K:
 rem = A % (N + 1)
 R[i] = rem
 A //= N + 1 
 i += 1
 
for num in R:
 print(num, end=' ')
print()


