from fractions import gcd

n = int(input())
x = list(map(int, input().split(' ')))
gcdx = x[0]
for i in x:
    gcdx = gcd(gcdx, i)

nums = max(x) / gcdx

if (int(nums) - n) % 2 == 1:
    print("Alice")
else:
    print("Bob")
