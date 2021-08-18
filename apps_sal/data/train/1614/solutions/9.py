def who_is_winner(moves):
    field = [[' ' for i in range(7)] for j in range(6)]

    for move in moves:
        column, color = move.split('_')

        field = place_color(field, column, color)
        result = check_win(field)

        if result:
            return result
    return 'Draw'


def check_win(field):
    field = list(reversed(field))

    for i in field:
        for j in range(4):
            h = set(i[j:4 + j])

            if h == {'R'}:
                return 'Red'
            elif h == {'Y'}:
                return 'Yellow'

    for i in range(3):
        for j in range(7):
            v = set([field[i + k][j] for k in range(4)])

            if v == {'R'}:
                return 'Red'
            elif v == {'Y'}:
                return 'Yellow'

    for i in range(3):
        for j in range(4):
            r = [field[i][j], field[i + 1][j + 1], field[i + 2][j + 2], field[i + 3][j + 3]]
            l = [field[i][-j - 1], field[i + 1][-j - 2], field[i + 2][-j - 3], field[i + 3][-j - 4]]

            if set(r) == {'R'} or set(l) == {'R'}:
                return 'Red'
            elif set(r) == {'Y'} or set(l) == {'Y'}:
                return 'Yellow'

    return 0


def place_color(field, column, color):
    index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}[column]

    for i in range(1, 7 + 1):
        if field[-i][index] == ' ':
            field[-i][index] = color[0]
            break

    return field
