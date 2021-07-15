keyboard = [
    "abcde123",
    "fghij456",
    "klmno789",
    "pqrst.@0",
    "uvwxyz_/",
]


def tv_remote(word):
    current_row, current_column = 0, 0
    total_moves = 0
    
    for letter in word:
        for row, line in enumerate(keyboard):
            column = line.find(letter)
            if column != -1:
                moves = abs(current_row - row) + abs(current_column - column) + 1 # +1 for OK button
                total_moves += moves
                current_row = row
                current_column = column
    return total_moves
