def doors(n):
    allDoors = []
    for i in range(0, n):
        allDoors.append("closed")

    for kid in range(1, n + 1):
        for door in range(kid - 1, n, kid):
            if allDoors[door] == "closed":
                allDoors[door] = "open"
            else:
                allDoors[door] = "closed"

    count = 0
    for j in range(0, len(allDoors)):
        if allDoors[j] == "open":
            count += 1
    return count
