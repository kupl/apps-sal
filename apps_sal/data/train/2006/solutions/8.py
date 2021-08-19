from fractions import gcd
n = int(input())
A = list(map(int, input().split()))
A.sort()
x = A[0]
for i in range(1, n):
    x = gcd(x, A[i])
moves = max(A) // x - n
if moves % 2 == 0:
    print('Bob')
else:
    print('Alice')
