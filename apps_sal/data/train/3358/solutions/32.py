def correct(string):
    string=list(string)
    for i in range(len(string)):
        if (isinstance(string[i],int))==True:
            pass
        else:
            if (string[i])=='0':
                string[i]='O'
            if (string[i])=='5':
                string[i]='S'
            if (string[i])=='1':
                string[i]='I'
    string=''.join(string)
    return string

