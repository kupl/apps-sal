for _ in range(int(input())):
    l = int(input())
    if l == 1:
        print(2)
        continue
    t_1 = list(bin(l)[2:])
    flag = 0
    for i in range(len(t_1) - 1, 0, -1):
        if flag == 1 and t_1[i] == '1':
            break
        if t_1[i] == t_1[i - 1] and t_1[i] == '1':
            continue
        else:
            flag = 1
    if flag == 1:
        print(-1)
        continue
    t_2 = t_1.count('1')
    t_3 = ((2**(t_2 - 1)) - 1)
    print(t_3)
