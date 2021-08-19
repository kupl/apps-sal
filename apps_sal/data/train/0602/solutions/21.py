try:
    a = input().split()
    l = [*[len(i) for i in a]]
    b = a[l.index(min(l))]
    print(b + ' ' + ' {} '.format(b).join(a) + ' ' + b)
except:
    pass
