def repeat_it(string,n):
    if type(string) != str: return "Not a string" 
    return_string = []
    for i in range(n):
        return_string.append(string)
    return "".join(return_string)

