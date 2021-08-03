let_to_num = {'A': [0, 5], 'B': [1, 6], 'C': [2, 7], 'D': [3, 8], 'E': [4, 9]}

num_to_let = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
              5: 'A', 6: 'B', 7: 'C', 8: 'D', 9: 'E'}

connections = {0: (1, 4, 5), 1: (0, 2, 6), 2: (1, 3, 7), 3: (2, 4, 8), 4: (0, 3, 9), 5: (0, 7, 8),
               6: (1, 8, 9), 7: (2, 5, 9), 8: (3, 5, 6), 9: (4, 6, 7)}

T = int(input())

for i in range(T):
    s = input()
    out_1, out_2 = [], []
    flag1, flag2 = True, True
    for c in range(len(s)):
        # print out_1, out_2, flag1, flag2
        if c == 0:
            out_1.append(let_to_num[s[c]][0])
            out_2.append(let_to_num[s[c]][1])
            # print out_1, out_2, '\n'
        else:
            if flag1:
                conn_1 = set(connections[out_1[-1]])
                to_conn_1 = set(let_to_num[s[c]])

                if len(conn_1.intersection(to_conn_1)) == 0:
                    flag1 = False
                else:
                    out_1.extend(list(conn_1.intersection(to_conn_1)))

                # print 'out1',conn_1, to_conn_1, flag1, conn_1.intersection(to_conn_1)
            if flag2:
                conn_2 = set(connections[out_2[-1]])
                to_conn_2 = set(let_to_num[s[c]])

                if len(conn_2.intersection(to_conn_2)) == 0:
                    flag2 = False
                else:
                    out_2.extend(list(conn_2.intersection(to_conn_2)))
                # print 'out2', conn_2, to_conn_2, flag2, conn_2.intersection(to_conn_2)
            # print out_1, out_2, flag1, flag2, '\n'
            if (not flag1) and (not flag2):
                break
    if (not flag1) and (not flag2):
        print(-1)
        continue
    elif flag1 and (not flag2):
        print(''.join(str(k) for k in out_1))
        continue
    elif flag2 and (not flag1):
        print(''.join(str(k) for k in out_2))
        continue
    else:
        print(min(''.join(str(k) for k in out_1), ''.join(str(k) for k in out_2)))
        continue
