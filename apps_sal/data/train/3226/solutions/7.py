def land_perimeter(arr):
    n = len(arr)
    m = len(arr[0])
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    ans = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'O':
                continue
            cur = 0
            for k in range(4):
                nx = i + dr[k]
                ny = j + dc[k]
                inside = (nx >= 0 and ny >= 0 and nx < n and ny < m)
                ans += (inside and arr[nx][ny] == 'O') + (not inside)
    ampogiko = "Total land perimeter: " + str(ans)
    return ampogiko
