t = int(input())
for i in range(t):
    (activities, origin) = input().split()
    s = 0
    for i in range(int(activities)):
        type = input().split()
        if type[0] == 'CONTEST_WON':
            s += 300
            rank = int(type[1])
            if rank < 20:
                s = s + (20 - rank)
        if type[0] == 'TOP_CONTRIBUTOR':
            s = s + 300
        if type[0] == 'BUG_FOUND':
            s = s + int(type[1])
        if type[0] == 'CONTEST_HOSTED':
            s = s + 50
    if origin == 'INDIAN':
        print(int(s / 200))
    if origin == 'NON_INDIAN':
        print(int(s / 400))
