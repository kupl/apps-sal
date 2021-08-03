def next_higher(value):
    c = bin(value).count('1')
    output_num = ''
    while True:
        value = value + 1
        if c == bin(value).count('1'):
            output_num = value
            break
    return output_num
