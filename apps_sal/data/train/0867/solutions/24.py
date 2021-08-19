for i in range(int(input())):
    (s, w1, w2, w3) = map(int, input().split())
    if s >= w1 + w2 + w3:
        print(1)
    elif s >= w1 + w2:
        if s >= w3:
            print(2)
        else:
            print(1 + w3 // s)
    elif s >= w2 + w3:
        if s >= w1:
            print(2)
        else:
            print(1 + w1 // s)
    else:
        print(w1 // s + w2 // s + w3 // s)
