def multi_table(number):
    t=['{0} * {1} = {2}'.format(i,number,i*number) for i in range(1,11)]
    return '\n'.join(t)
