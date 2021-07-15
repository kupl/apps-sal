def ones_counter(input):
    return [i.count('1') for i in ''.join(map(str, input)).split('0') if i]
