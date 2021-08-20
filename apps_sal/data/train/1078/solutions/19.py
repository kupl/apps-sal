for _ in range(int(input())):
    (s, w1, w2, w3) = list(map(int, input().split()))
    tot = w1 + w2 + w3
    if tot <= s:
        print(1)
    elif s == 1:
        print(3)
    elif s == 2:
        if tot >= 5:
            print(3)
        elif w2 == 2:
            print(3)
        else:
            print(2)
    elif s == 3:
        if tot <= 5:
            print(2)
        else:
            print(3)
    else:
        print(2)
