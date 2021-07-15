def basereduct(n):
    base_numbers = {'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 11}
    conversion = 0
    while len(str(n)) > 1:
        n = int(str(n), base_numbers[max(str(n))])
        conversion += 1
        if conversion > 150:
            return -1
    return n
