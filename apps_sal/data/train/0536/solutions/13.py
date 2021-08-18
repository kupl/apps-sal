for i in range(int(input())):
    NUMBER = input().split()
    CYBER_KIDS = int(NUMBER[0])
    WEAPONS = int(NUMBER[1])
    count = 0
    if WEAPONS < CYBER_KIDS:
        print(count)
    else:
        count = WEAPONS // CYBER_KIDS
        print(count)
