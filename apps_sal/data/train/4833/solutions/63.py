def replace_exclamation(s):
    new_s= ''
    for i in s:
        if i not in 'aeiouAEIOU':
            new_s= new_s + i
        if i in 'aeiouAEIOU':
            new_s= new_s + '!'
    return new_s
