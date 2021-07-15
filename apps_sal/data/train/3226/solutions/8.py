def land_perimeter(arr):
    per = 0
    for _ in range(4):
        arr.insert(0, ['0']*(len(arr[0])+(_+1)))
        arr = list(zip(*arr[::-1]))
    for i in range(1,len(arr)):
        for y in range(1,len(arr[i])):
            if arr[i][y] == 'X':
                per += 4 - sum([arr[i-1][y]=='X', arr[i+1][y]=='X', arr[i][y+1]=='X', arr[i][y-1]=='X'])
    return  f'Total land perimeter: {per}'
