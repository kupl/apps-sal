for i in range(eval(input())):
    lsum, rsum, n, bp = 0, 0, eval(input()), 0
    weights = input().split()
    weights = [int(x) for x in weights]
    for i in range(n):
        if sum(weights[0:i]) == sum(weights[i + 1::]):
            bp = 1
            break
    if bp == 1:
        print(i)
    else:
        print("-1")
