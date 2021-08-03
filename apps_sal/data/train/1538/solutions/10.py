def GCD(a, b):
    if(b == 0):
        return a
    else:
        return (GCD(b, a % b))


n = int(input())
for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    c = GCD(a, b)
    d = (a * b) // c
    print(c, d)
