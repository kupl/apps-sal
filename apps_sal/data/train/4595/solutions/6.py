import string
chars = [char for char in string.ascii_lowercase[:8]]
numbs = [char for char in string.digits[1:9]]
chessboard = {}
x = -1
for let in chars:
    x += 1
    y = 0
    for num in numbs:
        chessboard[let + num] = [x, y]
        y += 1


def bishop_diagonal(bishop1, bishop2):
    result = []
    same_diagonal = False
    bishop1_coord = chessboard[bishop1.lower()]
    bishop2_coord = chessboard[bishop2.lower()]
    directions = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
    for direction in directions:
        pos_coord = bishop1_coord[:]
        while pos_coord[0] > -1 and pos_coord[0] < 8 and (pos_coord[1] > -1) and (pos_coord[1] < 8) and (bishop2_coord != pos_coord):
            pos_coord[0] += direction[0]
            pos_coord[1] += direction[1]
            if bishop2_coord == pos_coord:
                direction_to_bishop2 = direction
                same_diagonal = True
    if same_diagonal:
        pos_coord = bishop2_coord[:]
        while pos_coord[0] > 0 and pos_coord[0] < 7 and (pos_coord[1] > 0) and (pos_coord[1] < 7):
            pos_coord[0] += direction_to_bishop2[0]
            pos_coord[1] += direction_to_bishop2[1]
        bishop2_to_field = pos_coord[:]
        direction_to_bishop1 = [x * -1 for x in direction_to_bishop2]
        pos_coord = bishop1_coord[:]
        while pos_coord[0] > 0 and pos_coord[0] < 7 and (pos_coord[1] > 0) and (pos_coord[1] < 7):
            pos_coord[0] += direction_to_bishop1[0]
            pos_coord[1] += direction_to_bishop1[1]
        bishop1_to_field = pos_coord[:]
        result.append(list(chessboard.keys())[list(chessboard.values()).index(bishop1_to_field)])
        result.append(list(chessboard.keys())[list(chessboard.values()).index(bishop2_to_field)])
        result.sort()
        return result
    else:
        result.append(bishop1)
        result.append(bishop2)
        result.sort()
        return result
