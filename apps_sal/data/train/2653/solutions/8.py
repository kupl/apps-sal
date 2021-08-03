def bingo(array):
    a = set()
    for x in array:
        if x == 2 or x == 9 or x == 14 or x == 7 or x == 15:
            a.add(x)
    return ("WIN" if len(a) >= 5 else "LOSE")
