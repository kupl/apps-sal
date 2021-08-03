def compute_depth(n):
    all_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    counter = 1
    while all_digits != []:
        for x in list(map(int, str(n * counter))):
            if x in all_digits:
                all_digits.remove(x)
        counter = counter + 1
    return counter - 1
