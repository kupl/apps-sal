test = int(input())
for i in range(test):
    user = input().split()
    activities = int(user[0])
    total = 0
    for j in range(activities):
        activ = input().split(' ')
        if activ[0] == 'CONTEST_WON':
            rank = int(activ[1])
            if rank <= 20:
                total += 320 - rank
            else:
                total += 300
        elif activ[0] == 'TOP_CONTRIBUTOR':
            total += 300
        elif activ[0] == 'BUG_FOUND':
            severity = int(activ[1])
            total += severity
        elif activ[0] == 'CONTEST_HOSTED':
            total += 50
    if user[1] == 'INDIAN':
        print(total // 200)
    else:
        print(total // 400)
