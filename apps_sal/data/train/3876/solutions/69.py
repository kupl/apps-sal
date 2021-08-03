def find(n):

    arr = []
    total = 0
    for i in range(n + 1):
        if i % 3 == 0:
            arr.append(i)
        elif i % 5 == 0:
            arr.append(i)

    for num in arr:
        total = total + num

    return total
