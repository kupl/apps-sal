def doors(n):
    door_status = []
    for a in range(0, n):
        door_status.append(False)
    for a in range(0, n):
        for b in range(a, n, a + 1):
            door_status[b] = not door_status[b]
    result = 0
    for a in range(0, n):
        if door_status[a] == True:
            result += 1
    return result
