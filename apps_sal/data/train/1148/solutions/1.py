tcase = int(input())
while tcase > 0:
    scores = []
    for test in range(3):
        points = list(map(int, input().split()))
        scores.append(points)
    scores = sorted(scores)
    answer = 'yes'
    count_01 = 0
    count_12 = 0
    for j in range(3):
        if scores[0][j] < scores[1][j]:
            count_01 = 1
        if scores[1][j] < scores[2][j]:
            count_12 = 1
        if (scores[0][j] > scores[1][j] or scores[1][j] > scores[2][j]):
            answer = 'no'
            break
        elif (count_01 == 0 or count_12 == 0) and j == 2:
            answer = 'no'
    print(answer)
    tcase -= 1
