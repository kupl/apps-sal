def find_variable():
    
    for var in globals():
        if eval(var) == 777:
            return var
