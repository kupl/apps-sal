for l in range(int(input())):
    p1, p2, k = list(map(int, input().split()))
    p = p1 + p2
    a = p // k
    if a % 2 == 0:
        print("CHEF")
    else:
        print("COOK")
