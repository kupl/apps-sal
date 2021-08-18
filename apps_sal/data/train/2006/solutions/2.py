
import fractions
n = int(input())
a = list(map(int, input().split()))
gcd = a[0]
for x in a:
    gcd = fractions.gcd(gcd, x)
moves = max(a) // gcd - n
print('Alice' if moves % 2 else 'Bob')
