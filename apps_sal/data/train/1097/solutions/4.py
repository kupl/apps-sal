for _ in range(eval(input())):
    n = eval(input())
    [l, b] = list(map(int, input().split()))
    for i in range(n):
        if l > b:
            l -= b
        elif b > l:
            b -= l
        else:
            l = b = 0
            break
        if b == 0 or l == 0:
            break
    if b == 0 or l == 0:
        print('No')
    else:
        print('Yes', l * b)
