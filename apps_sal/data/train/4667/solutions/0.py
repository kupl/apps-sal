def traffic_jam(road, sides):
    X = road.index('X')
    main = list(road[:X + 1])
    for i in reversed(range(min(X, len(sides)))):
        tmp = []
        for j in range(1, min(len(main) - i - 1, len(sides[i])) + 1):
            tmp.append(sides[i][-j])
            tmp.append(main[i + j])
        main[i + 1:i + len(tmp) // 2 + 1] = tmp
    return ''.join(main)
