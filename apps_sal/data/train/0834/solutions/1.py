t = int(input())
for _ in range(t):
    n, q = list(map(int, input().split()))
    main = [[0] * (n + 1)]
    final = [[0] * (n + 1)]
    const = [[0] * (n + 1)]
    for i in range(n):
        l = [0] * (n + 1)
        z = [0] * (n + 1)
        w = list(input().split())
        w.insert(0, 0)
        final.append(w)
        main.append(l)
        const.append(z)

    for i in range(1, n + 1):
        for j in range(1, n + 1):

            main[i][j] = max(main[i - 1][j], main[i][j - 1])
            if final[i][j] == 'a':
                main[i][j] += 1
            if main[i - 1][j] > main[i][j - 1]:
                const[i][j] += const[i - 1][j]
            else:
                const[i][j] += const[i][j - 1]
            if final[i][j] != 'a':
                const[i][j] += 1

    for i in range(q):
        s, d = list(map(int, input().split()))
        print(s + d - 1 - main[s][d])
