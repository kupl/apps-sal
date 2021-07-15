def encryptor (key, mess):
    lst = []
    for i in mess:
        if i.isalpha():
            C = 97 - 32 * i.isupper()
            lst.append (chr ((ord (i) - C + key)%26 + C))
        else:
            lst.append (i)
    return ''.join (lst)
