for _ in range(int(input())):
    x = list(input().split(' '))
    n = int(x[0])
    nationality = x[1]
    totalLaddus = 0
    for i in range(n):
        task = input().split(' ')
        if len(task) == 2:
            if task[0] == 'CONTEST_WON':
                rank = int(task[1])
                totalLaddus += 300
                if rank <= 20:
                    totalLaddus += 20 - rank
            elif task[0] == 'BUG_FOUND':
                totalLaddus += int(task[1])
        elif task[0] == 'CONTEST_HOSTED':
            totalLaddus += 50
        elif task[0] == 'TOP_CONTRIBUTOR':
            totalLaddus += 300
    if nationality == 'INDIAN':
        print(totalLaddus // 200)
    else:
        print(totalLaddus // 400)
