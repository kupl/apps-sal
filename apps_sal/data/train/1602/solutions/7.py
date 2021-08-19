try:
    t = int(input())
    for i in range(t):
        n = int(input())
        x = int(input())
        l = list(map(int, input().split()))
        if 1 in l:
            print('Impossible')
        else:
            l.sort()
            flag = False
            i = 0
            j = 0
            while i < max(l) - 1:
                ll = l[j:j + x]
                j = j + x
                if i + 1 in ll:
                    flag = True
                    break
                i = i + 1
            if flag:
                print('Impossible')
            else:
                print('Possible')
except:
    pass
