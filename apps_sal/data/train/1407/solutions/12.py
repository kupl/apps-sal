for _ in range(int(input())):
    (row, col) = map(int, input().split())
    if row == 1 and col == 1:
        print('1\n1')
    elif row == 1:
        if col > 2:
            print(2)
        else:
            print(1)
        ls = [1, 1, 2, 2]
        for i in range(col):
            print(ls[i % 4], end=' ')
        print()
    elif col == 1:
        if row > 2:
            print(2)
        else:
            print(1)
        ls = [1, 1, 2, 2]
        for i in range(row):
            print(ls[i % 4])
    elif col == 2:
        if row == 2:
            print('2\n1 2\n1 2')
        else:
            print(3)
            for j in range(row):
                for i in range(col):
                    print(j % 3 + 1, end=' ')
                print()
    elif row == 2:
        if col == 2:
            print('2\n1 2\n1 2')
        else:
            print(3)
            for j in range(2):
                for i in range(col):
                    print(i % 3 + 1, end=' ')
                print()
    else:
        first = [1, 1, 2, 2]
        second = [2, 2, 1, 1]
        third = [3, 3, 4, 4]
        fourth = [4, 4, 3, 3]
        first_found = 0
        second_found = 0
        temp = 0
        print(4)
        for i in range(row):
            for j in range(col):
                x = j % 4
                if temp % 2 == 0:
                    if first_found == 0:
                        print(first[x], end=' ')
                    else:
                        print(second[x], end=' ')
                elif second_found == 0:
                    print(third[x], end=' ')
                else:
                    print(fourth[x], end=' ')
            if first_found == 0 and temp % 2 == 0:
                first_found = 1
            elif first_found == 1 and temp % 2 == 0:
                first_found = 0
            if second_found == 0 and temp % 2 == 1:
                second_found = 1
            elif second_found == 1 and temp % 2 == 1:
                second_found = 0
            temp += 1
            print()
