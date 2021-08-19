def shuffle_it(char, *args):
    for arg in args:
        b = char[arg[0]]
        char[arg[0]] = char[arg[1]]
        char[arg[1]] = b
    return char
