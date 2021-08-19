import math
T = int(input())
while T > 0:
    (A, B) = map(int, input().split())
    hcf = math.gcd(A, B)
    lcm = A * B // hcf
    print(hcf, lcm)
    T = T - 1
