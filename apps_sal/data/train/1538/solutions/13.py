t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    dup1 = a
    dup2 = b
    while(b != 0):
        temp = b
        b = a % b
        a = temp
    gcd = int(a)
    lcm = int((dup1 * dup2) / gcd)
    print(gcd, lcm)
