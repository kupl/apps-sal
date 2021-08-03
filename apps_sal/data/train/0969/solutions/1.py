for i in range(int(input())):
    n, k = input().split()
    laddus = 0
    for j in range(int(n)):
        t = input().split()
        if t[0] == 'CONTEST_WON':
            if(int(t[1]) <= 20):
                laddus += 300 + 20 - int(t[1])
            else:
                laddus += 300
        elif t[0] == 'TOP_CONTRIBUTOR':
            laddus += 300
        elif t[0] == 'BUG_FOUND':
            laddus += int(t[1])
        elif t[0] == 'CONTEST_HOSTED':
            laddus += 50
    if(k == 'INDIAN'):
        print(laddus // 200)
    else:
        print(laddus // 400)
