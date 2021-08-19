# cook your dish here
try:
    for u in range(int(input())):
        n = int(input())
        li = []
        lid = []
        a = 1
        t = 0
        l = 0
        for i in range(n * n):
            t += 1
            lid.append(i + 1)
            if a == t:
                if l != -1:
                    a += 1
                    t = 0
                else:
                    a -= 1
                    t = 0
                li.append([int(k) for k in lid])
                lid.clear()
            if a == n:
                l = -1
        li2 = li.copy()
        for i in li:
            if len(li2) != 0:
                a = 0
                li3 = li2.copy()
                for j in li2:
                    if a == n:
                        break
                    a += 1
                    if len(j) != 0:
                        print(j[0], end=" ")
                        j.remove(j[0])
                li2.clear()
                li2 = li3.copy()
                if len(j) != 0:
                    print()
                else:
                    break
                li2.remove(li2[0])
        print()
except:
    pass
