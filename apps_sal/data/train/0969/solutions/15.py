t = int(input())
while t > 0:
    (n, s) = input().split()
    k = int(n)
    s1 = 0
    while k > 0:
        l = list(input().split())
        if l[0] == 'CONTEST_WON':
            if int(l[1]) < 20:
                s1 = s1 + (300 + (20 - int(l[1])))
            else:
                s1 = s1 + 300
        if l[0] == 'TOP_CONTRIBUTOR':
            s1 = s1 + 300
        if l[0] == 'BUG_FOUND':
            s1 = s1 + int(l[1])
        if l[0] == 'CONTEST_HOSTED':
            s1 = s1 + 50
        k = k - 1
    if s == 'INDIAN':
        print(s1 // 200)
    else:
        print(s1 // 400)
    t = t - 1
