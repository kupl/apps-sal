for _ in range(int(input())):
    num = int(input())
    if num < 10:
        print(num)
        continue
    digs = str(num)
    new = ''
    i = 1
    bad = False
    while i < len(digs):
        if digs[i - 1] > digs[i]:
            bad = True
            if digs[i - 1] != '1':
                new += str(int(digs[i - 1]) - 1) + '9' * (len(digs) - i)
            else:
                n = i - 1
                while n > 0 and digs[n] == '1':
                    n -= 1
                new = new[:n]
                new += str(int(digs[n]) - 1) + '9' * (len(digs) - n - 1)
            break
        else:
            new += digs[i - 1]
        i += 1
    if not bad:
        new = digs
    print(int(new))
