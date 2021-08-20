t = int(input())
for i in range(t):
    str = input()
    k = str.index('W')
    if len(str[:k]) == len(str[k + 1:]):
        print('Chef')
    else:
        print('Aleksa')
