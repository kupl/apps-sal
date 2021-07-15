def replace_exclamation(s):
    new = ''
    ls = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i.lower() not in ls:
            new += i
        else: 
            new += '!'
            
    return new
