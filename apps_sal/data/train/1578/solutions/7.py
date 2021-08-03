t = eval(input())
for x in range(0, t):
    arr = list(input())
    sum = 0
    for i in arr:
        if(i.isdigit()):
            sum += int(i)
    print(sum)
