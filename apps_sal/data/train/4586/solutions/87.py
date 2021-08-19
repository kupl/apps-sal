def tv_remote(word):
    keyboard = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    presses = 0
    pointer_pos = (0, 0)
    for i in word:
        letter_pos = keyboard.index(i)
        letter_pos = (letter_pos % 8, letter_pos // 8)
        presses += abs(letter_pos[0] - pointer_pos[0]) + abs(letter_pos[1] - pointer_pos[1]) + 1
        pointer_pos = letter_pos
    return presses
