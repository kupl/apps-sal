t = int(input())
for p in range(t):
    n = str(input())
    l = len(n)
    cnt = [0] * 10
    for i in range(l):
        if cnt[int(n[i])] < 2:
            cnt[int(n[i])] += 1
    output = []
    if cnt[6] > 0:
        for j in range(5, 10):
            if cnt[j] > 0 and j != 6:
                output.append(chr(6 * 10 + j))
            elif j == 6 and cnt[j] > 1:
                output.append(chr(66))
    if cnt[7] > 0:
        for j in range(0, 10):
            if cnt[j] > 0 and j != 7:
                output.append(chr(7 * 10 + j))
            elif j == 7 and cnt[j] > 1:
                output.append(chr(77))
    if cnt[8] > 0:
        for j in range(0, 10):
            if cnt[j] > 0 and j != 8:
                output.append(chr(8 * 10 + j))
            elif j == 8 and cnt[j] > 1:
                output.append(chr(88))
    if cnt[9] > 0:
        if cnt[0] > 0:
            output.append(chr(90))
    ops = ''.join(output)
    if len(ops) != 0:
        print(ops)
    else:
        print()
