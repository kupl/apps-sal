a = int(input())
for i in range(a):
    num = int(input())
    yes = 0
    while num > -1:
        if num % 7 == 0:
            print(num)
            yes = 1
            break
        else:
            num = num - 4
    if yes == 0:
        print(-1)
