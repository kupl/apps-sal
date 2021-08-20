t = int(input())
while t > 0:
    n = int(input())
    str1 = str(input()).split(' ')
    str1 = list(map(int, str1))
    output = 'No'
    totalCount = 0
    count = 0
    for i in str1:
        if i == 0:
            count += 1
            totalCount += 1
        elif i == 1 and count > 0:
            if count % 2 == 1 and totalCount != 1:
                output = 'Yes'
                break
            count = 0
    if str1[-1] == 0 and count % 2 == 1 and (totalCount != 1):
        output = 'Yes'
    if totalCount == 1:
        output = 'Yes'
    print(output)
    t = t - 1
