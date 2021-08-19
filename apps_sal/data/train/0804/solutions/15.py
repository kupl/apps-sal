try:
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a1 = a.copy()
        f = int(input())
        length_a = len(a)
        l1 = []
        l2 = []
        for j in range(length_a + 1):
            a = a1.copy()
            l = ['D', 0, 0]
            a.insert(j, l)
            k = 0
            l[2] = j + 1
            while len(a) != 2:
                length = len(a)
                if k >= length:
                    k = 0
                if a[k] == l:
                    k = k + 1
                    continue
                else:
                    m = k + 1
                    if m >= length:
                        m = 0
                    if a[m] == l:
                        l[1] += a[k]
                    else:
                        del a[m]
                    k += 1
            'if len(a)==2:\n                    if a[0]==l:\n                        l[1]+=f\n                    else:\n                        a[1]=a[1]-f\n                        \n                    if a[1]==l:\n                        l[1]+=f\n                    else:\n                        a[0]=a[0]-f\n                        if a[0]<0:\n                            l1.append(l)\n                '
            if a[0] == l:
                l[1] += f
            else:
                a[0] = a[0] - f
            if a[1] == l:
                l[1] += f
            else:
                a[1] = a[1] - f
            if a[0] != l:
                if a[0] <= 0:
                    l1.append(l)
                    l2.append(1)
                else:
                    l2.append(0)
            if a[1] != l:
                if a[1] <= 0:
                    l1.append(l)
                    l2.append(1)
                else:
                    l2.append(0)
        "if 1 in l2:\n                value=min(l1)\n                print('possible')\n                \n                print(value[2],value[1])\n        else:\n                print('impossible')\n                "
        if len(l1) > 0:
            value = min(l1)
            print('possible')
            print(value[2], value[1])
        else:
            print('impossible')
except:
    pass
