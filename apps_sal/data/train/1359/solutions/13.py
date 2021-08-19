for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    even = 0
    odd = 0
    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if n == 1:
        print(0)
    elif odd == 0 or even == 0:
        print(even + odd)
    else:
        x = (odd - 1) * 2 + even
        y = (even - 1) * 2 + odd
        print(min(x, y))
