def seven_ate9(x):
    i=0
    new_list=''
    while i < len(x):
        n_slice= x[i:i+3]
        if n_slice =='797':
            new_list = new_list + '7'
            i+=2
        else:
            new_list = new_list + x[i]
            i+=1
    return new_list
