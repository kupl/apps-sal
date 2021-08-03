def getlocation(letter):
    keyboard = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    return divmod(keyboard.find(letter), 8)


def tv_remote(word):
    x1, y1 = 0, 0
    moves = 0
    for letter in word:
        x2, y2 = getlocation(letter)
        moves += abs(x2 - x1) + abs(y2 - y1) + 1
        x1, y1 = x2, y2
    return moves
