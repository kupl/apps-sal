t = int(input())
while t:
    t = t - 1
    l = list(map(int, input().split()))
    S = l[0]
    W1 = l[1]
    W2 = l[2]
    W3 = l[3]
    hits = 0
    if W1 + W2 + W3 <= S:
        hits = 1
    elif W1 + W2 <= S:
        hits = 2
    elif W2 + W3 <= S:
        hits = 2
    else:
        hits = 3
    print(hits)
