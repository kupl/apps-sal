t = int(input())
for i in range(t):
    n = int(input())
    tubes = []
    for j in range(2):
        tubes.append(list(map(int, list(input()))))
    r = [0, 0]
    fl_ord = False
    while True:
        if tubes[r[0]][r[1]] <= 2:
            if fl_ord:
                print('NO')
                break
            else:
                r[1] += 1
        else:
            if fl_ord:
                r[1] += 1
            else:
                r[0] = 1 - r[0]
            fl_ord = not fl_ord
        if r == [1, n]:
            print('YES')
            break
        elif r == [0, n]:
            print('NO')
            break
