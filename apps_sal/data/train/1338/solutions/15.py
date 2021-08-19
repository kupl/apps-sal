l = list(map(float, input().split()))
for i in range(1, len(l), 2):
    res = str(round(l[i] * pow(10, l[i + 1]), 2))
    if int(res[-1]) == 0 and res[-2] == '.':
        print(str(round(l[i] * pow(10, l[i + 1]), 2)) + '0')
    else:
        print(round(l[i] * pow(10, l[i + 1]), 2))
