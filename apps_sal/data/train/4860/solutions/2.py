def amidakuji(ar):
    res = [0 for i in range(len(ar[0]) + 1)]
    for i in range(len(ar[0]) + 1):
        pos = i
        for j in range(len(ar)):
            if pos != 0 and ar[j][pos - 1] == '1':
                pos -= 1
            elif pos != len(ar[0]) and ar[j][pos] == '1':
                pos += 1
        res[pos] = i
    print(visualizer(ar))
    return res
