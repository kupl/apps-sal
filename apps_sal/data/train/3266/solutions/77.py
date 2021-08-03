def my_first_kata(a, b):
    if (isinstance(a or b, str) or (a == 0 or b == 0)):
        return False
    elif (isinstance(a and b, int)):
        if(str(a) == "True" or str(b) == "True" or int(a % b + b % a) == 0 or a == True and b == True):
            return False
        else:
            return int(a % b + b % a)
    else:
        return False
