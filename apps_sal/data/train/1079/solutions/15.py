t = int(input())
for i in range(t):
    a = int(input())
    count = 0
    while a != 0:
        if a % 10 == 4:
            count +=1
        a = a // 10
    print(count)
    

