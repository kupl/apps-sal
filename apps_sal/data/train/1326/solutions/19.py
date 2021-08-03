t = int(input())
for i in range(t):
    flag = 1
    n = int(input())
    f = [int(i) for i in input().split()]
    gas = 0
    for i in range(len(f)):
        gas += f[i]
        if gas == 0:
            print(i)
            flag = 0
            break
        gas -= 1
    if flag:
        print(sum(f))
