T = int(input())
for case in range(T):
    n = int(input())
    scores = [0] * n
    pitch = []
    for i in range(n):
        (l, u) = map(int, input().split())
        pitch.append((l, u))
    for i in range(n):
        for j in range(i + 1, n):
            if pitch[i][0] < pitch[j][0] and pitch[i][1] > pitch[j][1]:
                scores[i] += 2
            elif pitch[i][0] > pitch[j][0] and pitch[i][1] < pitch[j][1]:
                scores[j] += 2
            else:
                scores[i] += 1
                scores[j] += 1
    print(' '.join((str(a) for a in scores)))
