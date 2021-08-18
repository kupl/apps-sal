for afskafshjd in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    count = 0
    flag = 0
    for i in range(1, n):
        if b[i] < b[i - 1]:
            flag = 1
            break
        x = bin(b[i] & b[i - 1])

        count = count + x.count('1')
    if flag == 1:
        print('0')
        continue
    print((pow(2, count, 10**9 + 7)))
