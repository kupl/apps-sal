def solve(x):
    w = x.replace(' ', '')
    new_string = ''
    for i in range(1, len(w) + 1):
        new_string += w[-i]
    new_list = [f for f in x]
    start_at = 0
    spaces = []
    for val in new_list:
        if val == ' ':
            spaces.append(new_list.index(val, start_at))
            start_at = new_list.index(val, start_at) + 1
    for i in spaces:
        new_string = new_string[:i] + ' ' + new_string[i:]
    return new_string
