def correct_polish_letters(st): 
    check = {"ą" : "a",
            "ć" : "c",
            "ę" : "e",
            "ł" : "l",
            "ń" : "n",
            "ó" : "o",
            "ś" : "s",
            "ź" : "z",
            "ż" : "z"}
    str = ""
    for i in range(len(st)):
        if st[i] in check.keys():
            str += check.get(st[i])
        else:
            str += st[i]
    return str
