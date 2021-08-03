def find(n):
    count1 = 0
    count2 = 0
    for i in range(5, n + 1, 5):
        count2 += 1
        if count2 == 3:
            count2 = 0
            continue
        count1 += i
    for i in range(3, n + 1, 3):
        count1 += i
    return count1
