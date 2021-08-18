test = int(input())

x = list(map(int, input().strip().split()))

if(test == len(x)):
    x.sort()
    day = 1

    count = len(x) - 1
    while(count > 0):
        if(x[count - 1] == x[count]):
            count -= 1
        day += 1
        count -= 1

    print(day)
