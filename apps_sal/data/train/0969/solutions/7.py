for _ in range(int(input())):
    t = input().split()
    total = 0
    t[0] = int(t[0])
    for i in range(t[0]):
        l = input().split(" ")
        if(l[0] == "CONTEST_WON"):
            if(int(l[1]) <= 20):
                total += (20 - int(l[1])) + 300
            else:
                total += 300
        if(l[0] == "TOP_CONTRIBUTOR"):
            total += 300
        if(l[0] == 'BUG_FOUND'):
            total += int(l[1])
        if(l[0] == "CONTEST_HOSTED"):
            total += 50
    if(t[1] == "INDIAN"):
        print(total // 200)
    else:
        print(total // 400)
