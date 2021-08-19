# cook your dish here
tc = int(input())
for t in range(tc):
    n = int(input())
    tr = [''] * n
    nr = [''] * n
    ck = False
    for i in range(n):
        name = input()
        tim = int(input())
        if not ck:
            ck = True
            tr[0] = tim
            nr[0] = name
        else:
            tr[i] = tim
            nr[i] = name
            for j in range(i + 1):
                key = tr[j]
                kname = nr[j]
                k = j - 1
                while k >= 0 and tr[k] > key:
                    tr[k + 1] = tr[k]
                    nr[k + 1] = nr[k]
                    k = k - 1
                tr[k + 1] = key
                nr[k + 1] = kname
    print(*nr, sep='\n')
