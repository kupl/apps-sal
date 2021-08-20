def differentiate(eq, point):
    eq = eq.replace('-', ' -').strip()
    eq = eq.replace('+', ' +').strip()
    eq = eq.replace('-x', '-1x')
    eq = eq.replace('+x', '+1x')
    eq = eq.split(' ')
    eq = [i if i[0].isalpha() == False else '1' + i for i in eq]
    if 'x' not in eq[-1]:
        eq.pop(-1)
    for i in range(len(eq)):
        if eq[i][-1] == 'x':
            eq[i] = eq[i][:-1] + 'x^1'
        j = int(eq[i][-1])
        eq[i] = int(eq[i][:-3]) * j * point ** (j - 1)
    return sum(eq)
