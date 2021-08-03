def repeater(string, n):
    repeated_string = ''
    num_count = n
    while num_count > 0:
        repeated_string += string
        num_count -= 1
    return repeated_string
