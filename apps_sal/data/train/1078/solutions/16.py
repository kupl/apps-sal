for _ in range(int(input())):
    (s, w1, w2, w3) = list(map(int, input().split()))
    c = w1 + w2 + w3
    if s >= c:
        print(1)
    elif w1 + w2 <= s or w2 + w3 <= s:
        print(2)
    else:
        print(3)
