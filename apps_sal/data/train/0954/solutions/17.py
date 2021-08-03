t = int(input())
while t:
    n = int(input())
    z = ((n * (n + 1)) // 2)**2
    print(z * 2 - (n**3))
    t -= 1
