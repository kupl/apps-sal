def xor(a,b):
    #your code here
    # checking the a and b values for false - false respectively 
    if not a and not b:
        return False
    # checking the a and b values for true - false
    elif a and not b:
        return True
    # checking the a and b values for false - true
    elif not a and b:
        return True
    # checking the a and b values for true - true respectively 
    else:
        return False
