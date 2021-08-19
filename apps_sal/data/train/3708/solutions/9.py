d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def hex_to_dec(s):
    x = list(str(s.upper()))
    y = [d[i] for i in x][::-1]
    z = [16 ** i for i in range(len(y))]
    w = []
    for i in range(len(y)):
        w.append(y[i] * z[i])
    return sum(w)
