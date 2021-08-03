for _ in range(int(input())):
    p1, p2, k = map(int, input().split())
    s = p1 + p2 + 1
    if s % k == 0:
        c = s / k
    else:
        c = int(s / k) + 1
    if c % 2 == 0:
        print("COOK")
    else:
        print("CHEF")
