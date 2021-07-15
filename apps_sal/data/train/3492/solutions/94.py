p = {'ą':'a','ć':'c','ę':'e','ł':'l','ń':'n','ó':'o','ś':'s','ź':'z','ż':'z'}

def correct_polish_letters(st): 
    return ''.join([p.get(c, c) for c in st])
