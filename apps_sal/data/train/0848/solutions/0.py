T = int(input())
for i in range(T):
    (N, data) = (int(input()), list(map(int, input().split())))
    if N == 3:
        print(sum(data))
    else:
        best = data[0] + data[1] + data[2]
        overall = best
        k = len(data)
        for i in range(1, k - 2):
            overall = overall - data[i - 1] + data[i + 2]
            if overall > best:
                best = overall
        j = max(data[1], data[-2])
        l = data[-1] + data[0] + j
        if best < l:
            best = l
        print(best)
