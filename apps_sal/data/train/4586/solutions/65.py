keyboard = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'], ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]


def tv_remote(word):
    current_point = [0, 0]
    ret_val = 0
    for i in word:
        x = [x for x in keyboard if i in x][0]
        ret_val += abs(current_point[0] - keyboard.index(x)) + abs(current_point[1] - x.index(i)) + 1
        current_point = [keyboard.index(x), x.index(i)]
    return ret_val
