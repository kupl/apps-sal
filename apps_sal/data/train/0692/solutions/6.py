
def func(t, l, r):
    if t == 'U':
        try:
            a[l - 1] = r
        except:
            print('NA')
    elif t == 'A':
        try:
            print(sum(a[min(l - 1, r):max(l - 1, r)]))
        except:
            print('NA')
    elif t == 'M':
        try:
            print(max(a[min(l - 1, r):max(l - 1, r)]))
        except:
            print('NA')
    elif t == 'm':
        try:
            print(min(a[min(l - 1, r):max(l - 1, r)]))
        except:
            print('NA')
    elif t == 'S':
        try:
            bb = list(set(a[min(l - 1, r):max(l - 1, r)]))
            bb.sort()
            print(bb[-2])
        except:
            print('NA')
    elif t == 's':
        try:
            bb = list(set(a[min(l - 1, r):max(l - 1, r)]))
            bb.sort()
            print(bb[1])
        except:
            print('NA')
    else:
        print('!!!')


n = eval(input())
a = list(map(int, input().split()))
q = eval(input())

for i in range(q):
    t, l, r = input().split()
    try:
        func(t, int(l), int(r))
    except:
        print('!!!')
