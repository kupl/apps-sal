def ones_counter(input):
    return [ele.count('1') for ele in ''.join(map(str, input)).split('0') if ele.count('1')]
