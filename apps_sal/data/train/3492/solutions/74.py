def correct_polish_letters(st):
    dict = {'ą' : 'a', 'ć' : 'c','ę' : 'e', 'ł' : 'l', 'ń' : 'n', 'ó' : 'o', 'ś' : 's', 'ź' : 'z', 'ż' : 'z'}
    return ''.join([dict[x] if x in dict.keys() else x for x in st])
