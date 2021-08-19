n = int(input())
for i in range(n):
    p = int(input())
    turn = 1
    while p > 0:
        if p == 1:
            if turn % 2 == 0:
                print('A')
                break
            else:
                print('B')
                break
        elif p == 3:
            p = p - 1
            turn = turn + 1
        elif p % 2 == 0:
            if turn % 2 == 0:
                print('A')
                break
            else:
                print('B')
                break
        else:
            p = 3
            turn = turn + 1
