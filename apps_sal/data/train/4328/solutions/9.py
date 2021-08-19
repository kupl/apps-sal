def friend_find(line):
    s = 0
    for i in range(0, len(line) - 2):
        (f1, f2, f3) = (line[i], line[i + 1], line[i + 2])
        if [f1, f2, f3] == ['red', 'blue', 'blue']:
            s += 1
        elif [f1, f2, f3] == ['blue', 'red', 'blue']:
            s += 1
            line[i + 1] = ''
        elif [f1, f2, f3] == ['blue', 'blue', 'red']:
            s += 1
            line[i + 2] = ''
    return s
