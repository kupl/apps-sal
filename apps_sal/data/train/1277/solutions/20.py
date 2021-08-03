t = input()
t = int(t)
while t != 0:
    n = input()
    n = int(n)
    f = 0
    while n != 0:
        inp = input().split(" ")
        inp = [int(x) for x in inp]
        np = (inp[0] * inp[2] * 0.01) + inp[0]
        f += (inp[0] - (np - (np * inp[2] * 0.01))) * inp[1]
        n -= 1
    print(f)
    t -= 1
