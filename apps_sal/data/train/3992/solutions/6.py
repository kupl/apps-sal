def is_happy(n):
    if len(str(n))==1:
        return n in [1 , 7]
    else:
        return is_happy(sum([int(d)*int(d) for d in str(n)]))
