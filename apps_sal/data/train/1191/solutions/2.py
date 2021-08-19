t = int(input())
while t > 0:
    line = input().split()
    n = int(line[0])
    q = int(line[1])
    mylist = []
    while n > 0:
        s = input().strip()
        mylist.append(s)
        n -= 1
    while q > 0:
        m = input().strip()
        if m in mylist:
            print(m)
        else:
            for item in mylist:
                i = 0
                if len(item) == len(m):
                    while i < len(m) and item[i] == m[i]:
                        i += 1
                    i += 1
                    if item[i:len(item) - 1] == m[i:len(m) - 1]:
                        print(item)
                        break
                else:
                    while i < len(m) and item[i] == m[i]:
                        i += 1
                    if item[i + 1:len(item) - 1] == m[i:len(m) - 1]:
                        print(item)
                        break
        q -= 1
    t -= 1
