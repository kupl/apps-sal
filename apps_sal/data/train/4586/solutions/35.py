def tv_remote(word):
    characters = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'

    width = 8
    c_x = 0
    c_y = 0
    total_steps = 0
    for w in word:
        w_index = characters.find(w)
        w_x = (w_index % width)
        w_y = (w_index // width)

        w_x_steps = abs(w_x - c_x)
        w_y_steps = abs(w_y - c_y)
        w_steps = w_x_steps + w_y_steps + 1

        c_x = w_x
        c_y = w_y

        total_steps += w_steps

    return total_steps
