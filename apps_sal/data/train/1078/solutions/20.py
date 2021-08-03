for i in range(int(input())):
    s, w1, w2, w3 = map(int, input().split())
    c = 0
    sum = w1 + w2 + w3
    if w1 < w3:
        tmp = w3
        w3 = w1
        w1 = tmp
    if w1 + w2 + w3 <= s:
        print("1")
    elif w1 + w2 <= s:
        print("2")
    elif w1 <= s:
        c = c + 1
    if c == 1:
        if w2 + w3 <= s:
            print("2")
        elif w2 + w3 > s:
            print("3")
