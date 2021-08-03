def tv_remote(word):
    keyboard = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    horizontal_s = 0
    vertical_s = 0
    presses = 0
    for i in word:
        i_position = keyboard.find(i)
        horizontal = i_position % 8
        vertical = i_position // 8
        presses += (abs(horizontal - horizontal_s) + abs(vertical - vertical_s) + 1)
        horizontal_s = horizontal
        vertical_s = vertical
    return presses
