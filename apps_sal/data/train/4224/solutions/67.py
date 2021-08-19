def dont_give_me_five(start, end):
    s = [str(x) for x in range(start, end + 1)]
    d = '-'.join(s).replace('5', '!')
    f = d.split('-')
    result = []
    for x in f:
        if x.isdigit() == True:
            result.append(x)
    return len(result)
