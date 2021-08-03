try:
    n = int(input())
    for i in range(n):
        a = int(input())
        b = int(input())
        c = list(map(int, input().split()))
        if 1 in c:
            print("Impossible")
        else:
            c.sort()
            flag = False
            i = 0
            j = 0
            while i < max(c) - 1:
                c1 = c[j:j + b]
                j = j + b
                if i + 1 in c1:
                    flag = True
                    break
                i = i + 1
            if flag:
                print("Impossible")
            else:
                print("Possible")
except:
    pass
