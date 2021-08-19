for _ in range(int(input())):
    (n, orgin) = map(str, input().split())
    laddu = 0
    for _ in range(int(n)):
        i = list(input().split())
        if len(i) == 2:
            if 'CONTEST_WON' == i[0]:
                laddu += 300
                k = int(i[1])
                if k < 20:
                    laddu = 20 - k + laddu
            elif i[0] == 'BUG_FOUND':
                laddu += int(i[1])
        elif 'TOP_CONTRIBUTOR' == i[0]:
            laddu += 300
        elif i[0] == 'CONTEST_HOSTED':
            laddu += 50
    if orgin == 'INDIAN':
        print(laddu // 200)
    elif orgin == 'NON_INDIAN':
        print(laddu // 400)
