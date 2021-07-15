def replace_exclamation(s):
   # str = 'aeiouAEIOU'
    return s.translate(str.maketrans("aeiouAEIOU", "!!!!!!!!!!"))
