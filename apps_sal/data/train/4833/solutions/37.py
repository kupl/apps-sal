def replace_exclamation(s):
    tab = s.maketrans("aeiouAIEOU","!!!!!!!!!!","")
    return s.translate(tab)
