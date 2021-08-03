# cook your dish here
t = int(input())

while t:
    t -= 1
    n = int(input())

    print((n * (n + 1) * ((2 * n) + 1)) // 6)
