def remove_exclamation_marks(s):
    res = [i for i in s if i!='!']
    return ''.join(res)
