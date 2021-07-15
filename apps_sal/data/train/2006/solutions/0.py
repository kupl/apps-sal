def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
A = list(map(int, input().split()))

GCD = A[0]
for x in A[1:]:
    GCD = gcd(GCD, x)
num = max(A) // GCD - n
if num % 2 == 0:
    print("Bob")
else:
    print("Alice")


