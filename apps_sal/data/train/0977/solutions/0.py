try:
    for _ in range(int(input())):
        n = int(input())
        li = [i for i in input()]
        a = 0
        while a + 1 < len(li):
            li[a], li[a + 1] = li[a + 1], li[a]
            a += 2
        li2 = li.copy()
        for i in li2:
            fh = 109
            sh = 110
            li.remove(i)
            if ord(i) > fh:
                li.append(chr(fh - (ord(i) - sh)))
            else:
                li.append(chr(sh + (fh - ord(i))))
        for i in li:
            print(i, end="")
        print()
except:
    pass
