def add_binary(a,b):
    sum = a ++ b
    sum_bin = '{0:b}'.format(sum)
    return sum_bin
    
    
print(add_binary(5,1))
