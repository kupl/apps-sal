for _ in range(int(input())):
    n, c = list(map(int, input().split()))
    numpoints = 0
    moves = 0
    d = dict()
    for f in range(n):
        a, b = list(map(int, input().split()))
        dif = a - b
        mod = a % c
        if dif not in d:
            d[dif] = {}
        if mod not in d[dif]:
            d[dif][mod] = []
        d[dif][mod].append(a)
    for i in d:
        for j in d[i]:
            numpoints += 1
            num = len(d[i][j])
            d[i][j].sort()
            if num % 2:
                mid = d[i][j][int(num / 2)]
                for k in d[i][j]:
                    moves += abs(int((k - mid) / c))
            else:
                choice1 = 0
                mid = d[i][j][int(num / 2)]
                for k in d[i][j]:
                    choice1 += abs(int((k - mid) / c))
                choice2 = 0
                mid = d[i][j][int(num / 2) - 1]
                for k in d[i][j]:
                    choice2 += abs(int((k - mid) / c))
                moves += choice1
    print(numpoints, moves)
