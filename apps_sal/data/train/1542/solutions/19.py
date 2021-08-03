for _ in range(int(input())):
    sum = 0
    count = 0
    max = 0
    n = int(input())
    st = input()
    li = [int(i) for i in input().split(' ')]
    flag = True
    for i in range(n - 7):
        k = 0
        count = 1
        sum = 0
        for j in range(i, i + 8):
            if st[j] == 'd':
                sum += li[k] * 2
            elif st[j] == 't':
                sum += li[k] * 3
            elif st[j] == 'D':
                sum += li[k]
                count *= 2
            elif st[j] == 'T':
                sum += li[k]
                count *= 3
            else:
                sum += li[k]
            k += 1
        if flag == True:
            max = sum * count
            flag = False
        else:
            if sum * count > max:
                max = sum * count
    print(max)
