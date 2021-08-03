def last_digit(n1, n2):
    last_dict = {
        0: [0],
        1: [1],
        2: [2, 4, 6, 8],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]}

    if n2 == 0:
        return 1
    a = n1 % 10
    return last_dict[a][(n2 - 1) % len(last_dict[a])]
