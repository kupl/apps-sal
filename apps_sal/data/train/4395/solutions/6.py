def next_higher(value):
    value = list(bin(value)[2:][-1::-1])
    one = value.count('1')
    while True:
        tale = 1
        for i in range(len(value)):
            bite = str((int(value[i]) + tale) % 2)
            value[i] = bite
            tale = 1 if bite == '0' else 0
            if not tale:
                break
        if tale:
            value.append('1')
        if value.count('1') == one:
            break
    return int(''.join(value[-1::-1]), 2)
