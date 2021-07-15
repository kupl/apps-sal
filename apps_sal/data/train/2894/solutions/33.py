def triple_trouble(one, two, three):
    output = ''
    for first, second, third in zip(one, two, three):
        output = ''.join([output, first, second, third])
    return output
    #your code here

