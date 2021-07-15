def sum_str(a, b):
    if len(a)==0 and len(b)==0:
        return "0"
    elif len(a)==0: 
        return b
    elif len(b)==0:
        return a
    else:
        return f'{int(a)+int(b)}'

