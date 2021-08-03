n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
for i in range(0, q):
    t = input().split()
    L = int(t[1]) - 1
    R = int(t[2]) - 1
    if L < 0 or L >= len(a):
        print('!!!')
    elif t[0] == 'U':
        a[L] = R
    elif R < 0 or R >= len(a) or L > R:
        print('!!!')
    elif t[0] == 'A':
        print(sum(a[L:R + 1]))
    elif t[0] == 'M':
        x = list(set(a[L:R + 1]))
        print(max(x))
    elif t[0] == 'm':
        x = list(set(a[L:R + 1]))
        x.remove(max(x))
        try:
            print(max(x))
        except:
            print('NA')
    elif t[0] == 'S':
        x = list(set(a[L:R + 1]))
        print(min(x))
    elif t[0] == 's':
        x = list(set(a[L:R + 1]))
        x.remove(min(x))
        try:
            print(min(x))
        except:
            print('NA')
    else:
        print('!!!')
