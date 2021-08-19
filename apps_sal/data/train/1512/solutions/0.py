cases = int(input())
for _ in range(cases):
    (rows, cols) = map(int, input().split())
    if (cols - 1) % 3 == 0 and (rows - 1) % 4 == 0:
        print('Vanya')
    elif (cols - 1) % 3 != 0 and (rows - 1) % 4 == 0:
        print('Tuzik')
    elif (cols - 1) % 3 == 0 and (rows - 1) % 4 != 0:
        print('Tuzik')
    elif (cols - 1) % 3 == 1 and (rows - 1) % 4 == 1:
        print('Vanya')
    elif (cols - 1) % 3 == 2 and (rows - 1) % 4 == 2:
        print('Vanya')
    else:
        print('Tuzik')
