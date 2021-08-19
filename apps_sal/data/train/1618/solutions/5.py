def differentiate(equation, point):
    a = filter(lambda x: 'x' in x, equation.replace('-', '+-').split('+'))
    sum = 0
    for i in list(a):
        split_i = i.split('x')
        split_i[0] = split_i[0] + '1' if split_i[0] == '' or split_i[0] == '-' else split_i[0]
        split_i[1] = '^1' if split_i[1] == '' else split_i[1]
        sum += int(split_i[0]) * int(split_i[1][1:]) * point ** (int(split_i[1][1:]) - 1)
    return sum
