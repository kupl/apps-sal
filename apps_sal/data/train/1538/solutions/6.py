# cook your dish here
import math
t = int(input())
for i in range(0, t):
    (a, b) = map(int, input() .split())
    gcd = math.gcd(a,b)
    lcm = int((a*b)/gcd)
    print(gcd,lcm)
