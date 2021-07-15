def repeat_it(string,n):
    try:
        if string*n == str(string)*n:
            return string*n
        else:
            return "Not a string"
    except:
        return "Not a string"
