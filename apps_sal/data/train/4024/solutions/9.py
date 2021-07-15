def special_number(n):
    condition = str(n).translate(str(n).maketrans(dict.fromkeys('012345')))
    return 'Special!!' if not condition else 'NOT!!'
