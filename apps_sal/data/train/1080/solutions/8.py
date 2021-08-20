for t in range(int(input())):
    string = input()
    if len(string) == 1:
        print('YES')
    elif len(string) == 2:
        if string[0] != string[1]:
            print('YES')
        else:
            print('NO')
    elif len(string) > 2:
        first = string[0]
        second = string[1]
        if first == second:
            print('NO')
        else:
            flag = 1
            for i in range(2, len(string)):
                if i % 2 != 0:
                    if string[i] == second:
                        flag = 1
                    else:
                        flag = 0
                        break
                elif string[i] == first:
                    flag = 1
                else:
                    flag = 0
                    break
        if flag == 1:
            print('YES')
        else:
            print('NO')
