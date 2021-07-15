def tv_remote(word):
    matrix = [
             ['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
             ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
             ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
             ['p', 'q', 'r', 's', 't', '.', '@', '0'],
             ['u', 'v', 'w', 'x', 'y', 'z', '_', '/'],
             ['aA', ' '],
             ]

    vertical_inversion = {0:0, 1:1, 2:2, 3:3, 4:2, 5:1}
    horizontal_inversion = {0:0, 1:1, 2:2, 3:3, 4:4, 5:3, 6:2, 7:1}
    actions = ([0, 0],)
    upper_mode = False
    press_ok = 0
    func = lambda x, y: (vertical_inversion[abs(x[0]-y[0])] + horizontal_inversion[abs(x[1]-y[1])])

    for char in word:
        for i in range(6):
            if char.lower() in matrix[i]:
                if char.isupper() and not upper_mode:
                    actions += ([5, 0],)
                    upper_mode = True
                    press_ok += 1
                    actions += ([i, matrix[i].index(char.lower())],)
                    press_ok += 1
                elif char.isupper() and upper_mode:
                    actions += ([i, matrix[i].index(char.lower())],)
                    press_ok += 1
                elif char.islower() and upper_mode:
                    actions += ([5, 0],)
                    upper_mode = False
                    press_ok += 1
                    actions += ([i, matrix[i].index(char.lower())],)
                    press_ok += 1
                elif char.islower() and not upper_mode:
                    actions += ([i, matrix[i].index(char.lower())],)
                    press_ok += 1
                else:
                    actions += ([i, matrix[i].index(char.lower())],)
                    press_ok += 1

    return sum([func(i[0], i[1]) for i in list(zip(actions, actions[1:]))]) + press_ok
