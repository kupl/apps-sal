def repeater(string, n):
    counter = 0
    new_string = ''
    while counter < n:
        counter += 1
        new_string = new_string + string
    return new_string
