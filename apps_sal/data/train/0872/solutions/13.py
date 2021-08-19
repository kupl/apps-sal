n = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    l1 = list((_ for _ in range(1, l[0] + 1)))
    count = 0
    for j in l1:
        if j % l[1] == 0 and j % l[2] != 0:
            count += 1
        elif j % l[1] != 0 and j % l[2] == 0:
            count += 1
        if count >= l[3]:
            break
    if count >= l[3]:
        print('Win')
    else:
        print('Lose')
