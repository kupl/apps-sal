n = int(input())

a = list(map(int, input().split()))
h = int(input())
a.sort()
p = 0
mp = 0

l = n - 1
flag = True
c = 0

for x in a:
    while x > h and c < l:
        if p > 0:
            p = p - 1
            h = h + a[l]
            del a[l]
            l = l - 1
        else:
            flag = False
            break

    if x <= h and flag == True:
        c = c + 1
        h = h - x
        p = p + 1
        if p > mp:
            mp = p
    else:
        break

print(mp)
