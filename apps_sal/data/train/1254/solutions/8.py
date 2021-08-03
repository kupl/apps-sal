t = int(input())
for i in range(t):
    n, p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    cakewalk = 0
    difficulty = 0
    for i in range(len(a)):
        if(a[i] >= p // 2 and a[i] <= p):
            cakewalk = cakewalk + 1
        elif(a[i] >= 0 and a[i] <= p // 10):
            difficulty = difficulty + 1
    if(cakewalk == 1 and difficulty == 2):
        print("yes")
    else:
        print("no")
