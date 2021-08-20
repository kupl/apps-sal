x = int(input())
for i in range(x):
    y = list(map(str, input().split()))[:4]
    z = list(map(str, input().split()))[:4]
    m = 0
    for j in range(4):
        for k in range(4):
            if y[j] == z[k]:
                m += 1
    if m >= 2:
        print('similar')
    else:
        print('dissimilar')
