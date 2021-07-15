def correct_polish_letters(st): 
    dict = {"ą" : "a",
            "ć" : "c",
            "ę": "e",
            "ł" :"l",
            "ń" : "n",
            "ó" : "o",
            "ś" : "s",
            "ź" : "z",
            "ż" : "z"
    }
    word =""
    for i in st:
        if i.isupper()==True:
            word+=i
        else:
            word+= dict.get(i,i)
    return word
