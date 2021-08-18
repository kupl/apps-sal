n = int(input())
for i in range(0, n):
    c = 0
    l1 = list(map(str, input().split()))
    l2 = list(map(str, input().split()))
    for x in l1:
        if x in l2:
            c = c + 1
    if c >= 2:
        print("similar")
    else:
        print("dissimilar")
