def main():
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = int(input())
    r, g, bl = [], [], []
    used = set()
    for i in range(n):
        c1, c2 = a[i], b[i]
        if c1 == 1 or c2 == 1:
            r.append([p[i], i])
        if c1 == 2 or c2 == 2:
            g.append([p[i], i])
        if c1 == 3 or c2 == 3:
            bl.append([p[i], i])
    r.sort(reverse=True)
    g.sort(reverse=True)
    bl.sort(reverse=True)
    answer = []
    for i in list(map(int, input().split())):
        if i == 1:
            try:
                while True:
                    pop = r.pop()[0]
                    if pop not in used:
                        answer.append(str(pop))
                        used.add(pop)
                        break
            except:
                answer.append('-1')
        elif i == 2:
            try:
                while True:
                    pop = g.pop()[0]
                    if pop not in used:
                        answer.append(str(pop))
                        used.add(pop)
                        break
            except:
                answer.append('-1')
        elif i == 3:
            try:
                while True:
                    pop = bl.pop()[0]
                    if pop not in used:
                        answer.append(str(pop))
                        used.add(pop)
                        break
            except:
                answer.append('-1')
    print(' '.join(answer))


def __starting_point():
    main()


__starting_point()
