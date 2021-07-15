def repeat_it(string,n):
    return 'Not a string' if type(string)==int\
    or not string or string==False or string==True else n*string
