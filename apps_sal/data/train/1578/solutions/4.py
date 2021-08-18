t = int(input())
for i in range(t):
    l = list(input())
    count = 0
    for j in l:
        if(j.isdigit()):
            count = count + int(j)
    print(count)
