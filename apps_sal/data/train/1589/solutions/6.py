t = int(input())
while(t):
    t -= 1
    arr = [int(x) for x in input().split()]
    count = 0
    avg = []
    divv = []
    for i in range(len(arr)):
        if(arr[i] == -1):
            break
        else:
            if(arr[i] >= 30):
                count += 1
        if(arr[i] & 1 == 0):
            avg.append((i + 1) * arr[i])
            divv.append(i + 1)
    average = sum(avg) / sum(divv)
    print(count, '%.2f' % average)
