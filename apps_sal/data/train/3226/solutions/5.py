def land_perimeter(arr):
    total = 0
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] == 'X':
                total += 4
                if (x != len(arr) - 1) and (arr[x + 1][y] == 'X'):
                    total -= 1
                if (x != 0) and (arr[x - 1][y] == 'X'):
                    total -= 1
                if (y != len(arr[0]) - 1) and (arr[x][y + 1] == 'X'):
                    total -= 1
                if (y != 0) and (arr[x][y - 1] == 'X'):
                    total -= 1
    return 'Total land perimeter: %i' % total
