def tv_remote(word):
    keyboard = ['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']

    pos = (0, 0)
    count = 0
    for i in word:
        nextrow = None
        for row in keyboard:
            if i in row:
                nextrow = row

        newpos = (keyboard.index(nextrow), nextrow.index(i))
        count += abs(pos[0] - newpos[0]) + abs(pos[1] - newpos[1]) + 1
        pos = newpos

    return count
