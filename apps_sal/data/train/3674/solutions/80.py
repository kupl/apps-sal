def add_binary(a, b):
    s = a + b
    bins = [s % 2]
    while s > 1:
        s = s // 2
        bins.append(s % 2)
    final = ''
    for i in bins[::-1]:
        final += str(i)
    return final
