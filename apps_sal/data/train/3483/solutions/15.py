def string_parse(string):
    if not isinstance(string, str):
        return 'Please enter a valid string'
    letters = ['0']
    for i in string:
        if i == letters[-1][-1]:
            letters[-1] += i
        else:
            letters.append(i)
    return ''.join([i if len(i) < 3 else f'{i[:2]}[{i[2:]}]' for i in letters][1:])
