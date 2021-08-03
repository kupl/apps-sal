def last_digit(n1, n2):
    if n2 == 0:
        return 1
    seq = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
    l_digit = int(str(n1)[-1])
    position = n2 % len(seq[l_digit])
    return seq[l_digit][position - 1]
