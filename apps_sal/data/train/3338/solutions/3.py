def ones_counter(input):
    s = ''.join((str(i) for i in input)).split('0')
    return [[len(i) for i in s if len(i)], []][1 not in input]
