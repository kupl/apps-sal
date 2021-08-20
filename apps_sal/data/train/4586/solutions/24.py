def tv_remote(word):
    keyboard = ['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']
    cursor_position = [0, 0]
    total_moves = 0
    for char in word:
        for (i, row) in enumerate(keyboard):
            if char in row:
                new_position = [row.index(char), i]
                move = sum((abs(cursor_position[i] - new_position[i]) for (i, _) in enumerate(cursor_position))) + 1
                total_moves += move
                cursor_position = new_position
    return total_moves
