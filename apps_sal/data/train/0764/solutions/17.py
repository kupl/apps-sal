T = int(input())
for i in range(T):
    d1 = list(input().split())
    d2 = list(input().split())
    si = 0
    for i in d1:
        for j in d2:
            if i == j:
                si = si + 1
    if si >= 2:
        print('similar')
    else:
        print('dissimilar')
