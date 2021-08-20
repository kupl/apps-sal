try:
    tt = int(input())
    while tt:
        tt = tt - 1
        s = input()
        (st1, dicti, i) = ([], {}, 1)
        for j in s:
            if j == '(':
                st1.append(i)
            elif st1:
                h = st1.pop() - 2
                dicti[h + 2] = i
                while h >= 0 and s[h] == ')':
                    dicti[h + 1] = i
                    h -= 1
            i += 1
        q = int(input())
        t = list(map(int, input().split()))
        for i in t:
            if i in list(dicti.keys()):
                print(dicti[i])
            else:
                print(-1)
except:
    pass
