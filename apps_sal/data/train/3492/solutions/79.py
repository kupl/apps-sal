def correct_polish_letters(st): 
    list=[]
    dict={"ą":"a",
        "ć":"c",
        "ę":"e",
        "ł":"l",
        "ń":"n",
        "ó":"o",
        "ś":"s",
        "ź":"z",
        "ż":"z"}
    for i in st:
        if i in dict.keys():
            list.append(dict[i])
        elif st.isspace():
            list.append(" ")
        else:
            list.append(i)
    return "".join(list)
