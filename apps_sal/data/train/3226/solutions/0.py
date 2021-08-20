def land_perimeter(arr):
    (I, J) = (len(arr), len(arr[0]))
    P = 0
    for i in range(I):
        for j in range(J):
            if arr[i][j] == 'X':
                if i == 0 or arr[i - 1][j] == 'O':
                    P += 1
                if i == I - 1 or arr[i + 1][j] == 'O':
                    P += 1
                if j == 0 or arr[i][j - 1] == 'O':
                    P += 1
                if j == J - 1 or arr[i][j + 1] == 'O':
                    P += 1
    return 'Total land perimeter: ' + str(P)
