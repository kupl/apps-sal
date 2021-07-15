def correct_polish_letters(st): 
    # your code here
    alf={' ':' ','ą':'a','ć':'c','ę':'e','ł':'l','ń':'n','ó':'o','ś':'s','ź':'z','ż':'z'}
    return ''.join(alf[i] if i in alf else i for i in st)
