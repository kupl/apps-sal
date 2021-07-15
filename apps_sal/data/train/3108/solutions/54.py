def multi_table(number):
    return "\n".join(['{e} * {d} = {c}'.format(e=i,d=number,c=i*number) for i in range(1,11)])
