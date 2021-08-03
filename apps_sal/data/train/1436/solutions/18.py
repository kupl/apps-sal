for _ in range(int(input())):
    H = list(input())
    v = 1
    if H != H[::-1]:
        v += 1
    print(v)
