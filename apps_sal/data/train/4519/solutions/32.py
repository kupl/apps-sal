def max_number(n):
    #your code here
    to_return = sorted(str(n), reverse = True)
    
    return int("".join(to_return))

