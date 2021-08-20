def repeater(string, n):
    times_to_repeat = 0
    repeated_string = ''
    while times_to_repeat < n:
        repeated_string += string
        times_to_repeat += 1
    return repeated_string
