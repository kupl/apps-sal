for t in range(int(input())):
    numberlist = 0
    for n in range(int(input())):
        n, k = list(map(int, input().split()))
        if abs(n - k) > 5:
            numberlist += 1
    print(numberlist)
