def tv_remote(word):
    keypad = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    list(keypad)
    list(word)
    indices = [keypad.index(letter) for letter in word]
    coord_x = [ind % 8 for ind in indices]
    coord_x.insert(0, 0)
    coord_y = [int(ind / 8) for ind in indices]
    coord_y.insert(0, 0)

    steps_x = [abs(coord_x[i + 1] - coord_x[i]) for i in range(len(coord_x) - 1)]
    steps_y = [abs(coord_y[i + 1] - coord_y[i]) for i in range(len(coord_y) - 1)]

    presses = [steps_x[i] + steps_y[i] + 1 for i in range(len(steps_x))]

    return sum(presses)
