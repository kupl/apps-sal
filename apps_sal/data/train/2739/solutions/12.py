def cube_odd(arr):
    odds = []
    for num in arr:
        if type(num) != type(4):
            return None
        elif num % 2 != 0:
            odds.append(num ** 3)
    return sum(odds)
