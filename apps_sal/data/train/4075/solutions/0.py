from functools import reduce
def product(ar):
    return reduce(lambda x,y:x*y, ar)

def something_acci(num_digits):
    seq = [1, 1, 2, 2, 3, 3]
    
    while(len(str(seq[-1])) < num_digits):
        seq.append(product(seq[-3:]) - product(seq[-6:-3]))
    
    return (len(seq), len(str(seq[-1])))

