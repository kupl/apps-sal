for T in range(int(input())):
    (n, ind) = input().split()
    n = int(n)
    laddu = 0
    for i in range(n):
        ls = list(input().split())
        if len(ls) == 2:
            if ls[0] == 'CONTEST_WON':
                k = int(ls[1])
                if 20 >= k:
                    laddu = laddu + (300 + (20 - k))
                else:
                    laddu = 300 + laddu
            elif ls[0] == 'BUG_FOUND':
                d = int(ls[1])
                laddu = laddu + d
        elif ls[0] == 'TOP_CONTRIBUTOR':
            laddu = laddu + 300
        else:
            laddu = laddu + 50
    if ind == 'INDIAN':
        print(laddu // 200)
    else:
        print(laddu // 400)
