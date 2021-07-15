def max_multiple(divisor, bound):
    a=bound
    print(( divisor,a))
    while a>divisor:
        if a%divisor==0 and a>0:
            return a
        else :
            a=a-1
            if a%divisor==0 and a>0:
                return a

        

