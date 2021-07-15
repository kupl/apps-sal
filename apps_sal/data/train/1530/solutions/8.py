for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    ctr = 1
    lis = []
    temp = 1
    for i in range(n):
        for j in range(temp):
            lis.append(ctr)
            ctr += 1
        temp += 1
        lis.reverse()
        lis = list(map(str, lis))
        print(''.join(lis))
        lis = []
