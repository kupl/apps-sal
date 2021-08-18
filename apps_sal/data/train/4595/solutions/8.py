def bishop_diagonal(bishop1, bishop2):

    board = [i + str(j) for i in 'abcdefgh' for j in range(1, 9)]

    diagonal1 = [m for m in board if abs(ord(m[0]) - ord(bishop1[0])) == abs(int(m[1]) - int(bishop1[1]))]
    diagonal2 = [m for m in board if abs(ord(m[0]) - ord(bishop2[0])) == abs(int(m[1]) - int(bishop2[1]))]
    diagonal = list(set(diagonal1).intersection(set(diagonal2)))

    if abs(ord(bishop1[0]) - ord(bishop2[0])) == abs(int(bishop1[1]) - int(bishop2[1])):

        top = [m for m in diagonal if int(m[1]) == max([int(i[1]) for i in diagonal])][0]
        bottom = [m for m in diagonal if int(m[1]) == min([int(i[1]) for i in diagonal])][0]
        return sorted([top, bottom])

    else:
        return sorted([bishop2, bishop1])
