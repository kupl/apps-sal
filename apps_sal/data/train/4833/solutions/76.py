def replace_exclamation(s):
    vow = 'aeiouAEIOU'
    a = ''
    for i in s:
        if i in vow:
            a += "!"
        else:
            a += i
    return a
