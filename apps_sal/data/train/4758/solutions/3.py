def place(table, pos, arg):
    for i in range(6):
        if table[5 - i][pos] == '-':
            table[5 - i][pos] = arg
            break


def connect_four_place(columns):
    table = [['-' for i in range(7)] for j in range(6)]
    for i in range(len(columns)):
        if i % 2 == 0:
            place(table, columns[i], 'Y')
        else:
            place(table, columns[i], 'R')
    return table
