def arbitrate(input, n):
    i =input.find('1')
    return input[:i+1]+'0'*len(input[i+1:])
