# cook your dish here
import math
for _ in range(int(input())):
 m, b = map(int,input().split())
 print(2*math.gcd(m, b))
