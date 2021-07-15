def array(string):
    result = ""
    x = string.split(',')
    if len(x) < 3:
        return None
    else:
        for i in range(1, len(x)-1):
            result += x[i] + " "
        return result[:-1]
    

