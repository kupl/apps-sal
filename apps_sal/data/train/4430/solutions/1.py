import re

def vowel_2_index(string):
    return re.sub("[aeiou]",lambda m:str(m.end()),string,0,re.I)
