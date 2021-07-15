def repeat_it(string,n):
    str = ''
    bool = False
    for i in range(n):
        try:
            str += string
        except: 
            bool = True
            return 'Not a string'
    if bool == False:
        return str
