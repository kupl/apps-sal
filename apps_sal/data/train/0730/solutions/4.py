t = int(input())
for i in range(t):
    n = int(input())
    final = 0
    winner = 0
    count = 0
    winnerPoints = [0] * (n + 1)
    for j in range(n):
        c = [int(num) for num in input().strip().split()]
        arr = [0] * 7
        for k in range(1, c[0] + 1):
            arr[c[k]] += 1
        arr.sort()
        six = arr[1]
        five = arr[2] - six
        four = arr[3] - five - six
        point = six * 4 + five * 2 + four * 1 + c[0]
        if point > final:
            final = point
            winner = j + 1
        winnerPoints[j + 1] = point
    for tr in range(1, n + 1):
        if winnerPoints[tr] == final:
            count += 1
    if count > 1:
        print('tie')
    elif winner == 1:
        print('chef')
    else:
        print(str(winner))
