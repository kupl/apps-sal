def target_game(arr):
    a = 0
    b = 0

    for i in arr:

        newA = a if (a > b) else b

        b = a + i
        a = newA

    if (a > b):
        return a
    else:
        return b
