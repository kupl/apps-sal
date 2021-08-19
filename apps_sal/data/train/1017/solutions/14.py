for i in range(int(input())):
    numberlist = list(map(int, input().split()))
    timelist = numberlist[:-1]
    p = numberlist[-1]
    for i in range(len(timelist)):
        timelist[i] *= p
    if sum(timelist) <= 120:
        print('No')
    else:
        print('Yes')
