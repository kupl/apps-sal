t = int(input())
for p in range(0, t):
    a, n = input().split()
    l = 0
    for i in range(0, int(a)):
        c = [z for z in input().split(' ')]
        if(c[0][8] == 'W'):
            l = l + 300
            if(int(c[1]) <= 20):
                l = l + 20 - int(c[1])
        elif(c[0][0] == 'T'):
            l = l + 300
        elif(c[0][0] == 'B'):
            if(int(c[1]) >= 50 and int(c[1]) <= 1000):
                l = l + int(c[1])
        elif(c[0][8] == 'H'):
            l = l + 50
        c.clear()
    if(n == 'INDIAN'):
        print(l // 200)
    else:
        print(l // 400)
