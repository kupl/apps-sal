def count_sheep(n):
    # your code
    
    x = 1
    list = []
    
    
    while x <= n:
        sheep = "{} sheep...".format(x)
        list.append(sheep)
        x += 1    
    
    return "".join(list)
