def correct_polish_letters(st): 
    dict = { "ą" : "a",
"ć" : "c",
"ę" : "e",
"ł" : "l",
"ń" : "n",
"ó" : "o",
"ś" : "s",
"ź" : "z",
"ż" : "z" }
    st2= ""
    for ch in st:
        if ch in dict:
            st2= st2+(dict[ch])
        else:
            st2= st2+(ch)
    
    
    return st2

