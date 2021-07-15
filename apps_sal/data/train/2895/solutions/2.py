def ka_co_ka_de_ka_me(word):
    prdel = "";
    for i, x in enumerate(word):
        if i != len(word):
            if x.lower() not in "aeiou" and word[i-1].lower() in "aeiou" and i != 0:
                prdel += "ka"
        prdel += x
    
    return "ka" + prdel
