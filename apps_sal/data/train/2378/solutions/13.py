a = int(input())
for i in range(a):
    b = input()
    l = [0, 0, 0, 0]
    for i in b:
        if i == 'U':
            l[0] += 1
        elif i == 'D':
            l[1] += 1
        elif i == 'R':
            l[2] += 1
        else:
            l[3] += 1
    ans1 = min(l[0], l[1])
    ans2 = min(l[2], l[3])
    if ans1 != 0 and ans2 != 0:
        print(2 * ans1 + 2 * ans2)
        k = 'U' * ans1 + "R" * ans2 + "D" * ans1 + "L" * ans2
        print(k)

    else:
        if ans2 > 0:
            print(2)
            print('RL')
        elif ans1 > 0:
            print(2)
            print('UD')
        else:
            print(0)
