for _ in range(int(input())):
    (s, w1, w2, w3) = map(int, input().split())
    if w1 + w2 + w3 <= s:
        ans = 1
    elif w1 + w2 <= s or w2 + w3 <= s:
        ans = 2
    else:
        ans = 3
    print(ans)
