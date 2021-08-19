for h in range(int(input())):
    (s, w1, w2, w3) = map(int, input().split())
    sum1 = w1 + w2 + w3
    if s >= sum1:
        print(1)
    elif s >= w1 + w2 or s >= w3 + w2:
        print(2)
    else:
        print(3)
