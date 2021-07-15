def table_game(table):
    top_left, top_right, bot_left, bot_right = table[0][0], table[0][-1], table[-1][0], table[-1][-1]
    top, bot, left, right = table[0][1], table[-1][1], table[1][0], table[1][-1]
    center = table[1][1]
    if (top_left + top_right == top and
        bot_left + bot_right == bot and
        top_left + bot_left == left and
        top_right + bot_right == right and
        top + bot == center):
        return [top_left, top_right, bot_left, bot_right]
    else:
        return [-1]
