def func(t, l, r):
    if t == 'U':
        try:
            a[l - 1] = r
        except:
            print('NA')
            return ''
    elif t == 'A':
        try:
            print(sum(a[l - 1:r]))
        except:
            print('NA')
            return ''
    elif t == 'M':
        try:
            print(max(a[l - 1:r]))
        except:
            print('NA')
            return ''
    elif t == 'm':
        try:
            print(min(a[l - 1:r]))
        except:
            print('NA')
            return ''
    elif t == 'S':
        try:
            bb = list(set(a[l - 1:r]))
            bb.sort()
            print(bb[-2])
        except:
            print('NA')
            return ''
    elif t == 's':
        try:
            bb = list(set(a[l - 1:r]))
            bb.sort()
            print(bb[1])
        except:
            print('NA')
            return ''
    else:
        print('!!!')


n = eval(input())
a = list(map(int, input().split()))
q = eval(input())
for i in range(q):
    (t, l, r) = input().split()
    func(t, int(l), int(r))
