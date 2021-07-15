def multi_table(number):
    res = ''
    for i in range(10):
        res += (f'{i+1} * {number} = {number*(i+1)}')
        if i < 9:
            res += '\n'
    return(res)
