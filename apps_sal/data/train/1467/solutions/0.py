# cook your dish here
def guessingGame(l):
    a = []
    m = 1000000001
    for i in range(len(l)):
        k = int(l[i][1])
        if (l[i][0] == '<' and l[i][2] == 'Yes'):
            a.append((1, 1))
            a.append((k, -1))

        if (l[i][0] == '<' and l[i][2] == 'No'):
            a.append((k, 1))
            a.append((m, -1))

        if (l[i][0] == '=' and l[i][2] == 'Yes'):
            a.append((k, 1))
            a.append((k + 1, -1))

        if (l[i][0] == '=' and l[i][2] == 'No'):
            a.append((1, 1))
            a.append((k, -1))
            a.append((k + 1, 1))
            a.append((m, -1))

        if (l[i][0] == '>' and l[i][2] == 'Yes'):
            a.append((k + 1, 1))
            a.append((m, -1))

        if (l[i][0] == '>' and l[i][2] == 'No'):
            a.append((1, 1))
            a.append((k + 1, -1))

    a.sort()
    w = 0
    r = 0

    for i in range(len(a)):
        w += a[i][1]
        r = max(w, r)

    return len(l) - r


def __starting_point():

    T = int(input())
    answer = []

    for _ in range(T):
        e = int(input())
        temp = []
        for q_t in range(e):
            q = list(map(str, input().rstrip().split()))
            temp.append(q)
        result = guessingGame(temp)
        print(result)


__starting_point()
