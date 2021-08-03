for i in range(int(input())):
    n = int(input())
    b = []
    counter = 0
    for j in range(n):
        b.append(list(map(int, input().split())))
    c = max(b[-1])
    sum = c
    for k in range(1, n):
        for x in b[-k - 1]:
            if(x < c and x > counter):
                counter = x
        if(counter == 0):
            print(-1)
            sum = 0
            break
        else:
            sum = sum + counter
            c = counter
            counter = 0
    if(sum != 0):
        print(sum)
