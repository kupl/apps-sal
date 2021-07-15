def string_clean(s):
    """
    Function will return the cleaned string
    """
    phrase = ""
    for i in range(len(s)):
        if s[i].isnumeric()!= True:
            phrase+=s[i]
    return phrase
