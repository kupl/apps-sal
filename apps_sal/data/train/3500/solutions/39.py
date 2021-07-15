def remove_exclamation_marks(s):
    a=''
    for i in s:
        if i=='!':
            a=a+''
        else:
            a=a+i
    return a
