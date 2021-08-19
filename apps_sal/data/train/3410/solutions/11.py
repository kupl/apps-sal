def scratch(lottery):
    # your code here
    sum = 0

    for x in lottery:
        j = x.split()
        if j[0] == j[1] == j[2]:
            sum += int(j[3])
    return sum
