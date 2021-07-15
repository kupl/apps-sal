def capitalize(s,ind):
    s1=[i for i in s]
    for indeks in range(0,len(s)):
        if indeks in ind:
            s1[indeks]=s1[indeks].upper()
    return ''.join(s1)     
