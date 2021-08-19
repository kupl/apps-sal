for _ in range(int(input())):
    n = int(input())
    plum = [list(map(int, list(input()))), list(map(int, list(input())))]
    h = 0
    answer = 'YES'
    for i in range(n):
        if plum[h][i] > 2:
            if plum[(h + 1) % 2][i] > 2:
                h = (h + 1) % 2
            else:
                answer = 'NO'
                break
    if h != 1:
        answer = 'NO'
    print(answer)
