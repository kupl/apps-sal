def tv_remote(word):
    characters = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'

    width = 8             # keypad width
    c_x = 0               # index of cursor starting location
    c_y = 0
    total_steps = 0       # running sum of steps
    for w in word:
        # find co-ords of w
        w_index = characters.find(w)
        w_x = (w_index % width)       # column number
        w_y = (w_index // width)      # row number

        # compare to cursor co-ordinates
        w_x_steps = abs(w_x - c_x)
        w_y_steps = abs(w_y - c_y)
        w_steps = w_x_steps + w_y_steps + 1     # extra for 'OK' button

        # update cursor
        c_x = w_x
        c_y = w_y

        # running total
        total_steps += w_steps

    return total_steps
