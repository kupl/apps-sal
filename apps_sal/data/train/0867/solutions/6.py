t = int(input())
for i in range(t):
    r = [int(x) for x in input().split()]
    [s, w1, w2, w3] = r
    x = 0
    if sum(r) <= s:
        print(1)
    elif w1 + w2 <= s or w2 + w3 <= s:
        print(2)
    else:
        print(3)
