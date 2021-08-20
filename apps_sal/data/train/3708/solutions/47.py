def hex_to_dec(s):
    case = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    s = list(s)
    s.reverse()
    (sum_, j) = (0, 0)
    for i in range(len(s)):
        sum_ += case.get(s[i]) * pow(16, j)
        j += 1
    return sum_
