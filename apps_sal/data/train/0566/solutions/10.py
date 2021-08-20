t = int(input())
for _ in range(t):
    a = str(input())
    b = str(input())
    k = 0
    for i in a:
        for j in b:
            if i == j:
                k += 1
    if k > 0:
        print('Yes')
    else:
        print('No')
