T = int(input())
while(T != 0):
    t = int(input())
    sum = 0
    while(t != 0):
        a = t % 10
        sum = sum + a
        t = t // 10
    print(sum)
    T -= 1
