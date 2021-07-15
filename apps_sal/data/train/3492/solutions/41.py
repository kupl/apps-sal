correct_polish_letters = lambda st: ''.join([{'ą':'a','ć':'c','ę':'e','ł':'l','ń':'n','ó':'o','ś':'s','ź':'z','ż':'z'}.get(i,i) for i in st])
