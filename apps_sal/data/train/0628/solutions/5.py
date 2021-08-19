# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        s = input()
        l = len(s)
        k = l // 2
        if (len(s) % 2 != 0 and s[k] == 'W'):
            print('Chef')
        else:
            print('Aleksa')
except:
    pass
