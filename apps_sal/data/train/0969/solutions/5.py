t = int(input())
for _ in range(t):
    (n, s) = list(map(str, input().split()))
    n = int(n)
    laddus = 0
    for i in range(n):
        x = input().split()
        if x[0] == 'CONTEST_WON':
            if int(x[1]) <= 20:
                laddus += 320 - int(x[1])
            else:
                laddus += 300
        elif x[0] == 'TOP_CONTRIBUTOR':
            laddus += 300
        elif x[0] == 'BUG_FOUND':
            laddus += int(x[1])
        elif x[0] == 'CONTEST_HOSTED':
            laddus += 50
    if s == 'INDIAN':
        months = laddus // 200
    if s == 'NON_INDIAN':
        months = laddus // 400
    print(months)
