for _ in range(int(input())):
    a = input().split()
    total = 0
    for i in range(int(a[0])):
        x = input().split()
        if x[0] == 'CONTEST_WON':
            if int(x[1]) < 20:
                total += 20 - int(x[1])
            total += 300
        elif x[0] == 'TOP_CONTRIBUTOR':
            total += 300
        elif x[0] == 'BUG_FOUND':
            total += int(x[1])
        elif x[0] == 'CONTEST_HOSTED':
            total += 50
    if a[1] == 'INDIAN':
        print(total // 200)
    elif a[1] == 'NON_INDIAN':
        print(total // 400)
