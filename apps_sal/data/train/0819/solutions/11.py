# cook your dish here
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for test in range(int(input())):
    a = [int(s) for s in input().split()]
    if gcd(a[0], a[1]) == 1: print("YES")
    else: print("NO")
