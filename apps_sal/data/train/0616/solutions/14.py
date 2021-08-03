# cook your dish here
T = int(input())

for i in range(T):
    m, n = input().split()
    m = int(m)
    n = int(n)
    c = []
    # m = 4
    # n  = 5
    # c = [['N', 'P', 'N', 'N', 'P'], ['N', 'N', 'P', 'N', 'N'], ['N', 'P', 'N',         'N', 'N'], ['P', 'N', 'N', 'N', 'N']]
    start_pos_m = -1
    start_pos_n = -1
    for j in range(m):
        c.append(input().split())
        if('P' in c[-1] and start_pos_m == -1):
            start_pos_n = c[-1].index('P')
            start_pos_m = j
    # print(c)
    cur_pos_m = start_pos_m
    cur_pos_n = start_pos_n
    next_pos_m = cur_pos_m
    number_of_steps = 0
    next_pos_n = start_pos_n
    for j in range(start_pos_m, m - 1):
        if('P' not in c[j]):
            if(j % 2 == 0):
                if('P' in c[j + 1][next_pos_n + 1: n]):
                    print(1)
                    rev = c[j + 1][:: -1]
                    next_pos_n = n - 1 - rev.index('P')
                    number_of_steps += next_pos_n - cur_pos_n
                    cur_pos_n = next_pos_n
            else:
                if('P' in c[j + 1][0: next_pos_n]):
                    next_pos_n = c[j + 1].index('P')
                    number_of_steps += cur_pos_n - next_pos_n
                    cur_pos_n = next_pos_n
            if('P' in c[j + 1]):
                number_of_steps += j - cur_pos_m
            # print(c[j])

        elif(j % 2 == 0):
            rev = c[j][:: -1]
            next_pos_n = n - 1 - rev.index('P')
            if('P' in c[j + 1][next_pos_n: n]):
                rev = c[j + 1][:: -1]
                next_pos_n = n - 1 - rev.index('P')
            number_of_steps += next_pos_n - cur_pos_n
            cur_pos_n = next_pos_n
            number_of_steps += 1
        else:
            # rev = c[j][:: -1]
            # print("rev : ", rev)
            next_pos_n = c[j].index('P')
            if('P' in c[j + 1][0: next_pos_n + 1]):
                next_pos_n = c[j + 1].index('P')
            number_of_steps += cur_pos_n - next_pos_n
            cur_pos_n = next_pos_n
            number_of_steps += 1
        cur_pos_m = j

    if(m % 2 == 0):
        if('P' in c[-1][0: cur_pos_n]):
            number_of_steps += cur_pos_n - c[-1][0: cur_pos_n].index('P')
    else:
        if('P' in c[-1][cur_pos_n + 1::]):
            number_of_steps += n - 1 - c[-1][:: -1].index('P') - cur_pos_n

    print(number_of_steps)
