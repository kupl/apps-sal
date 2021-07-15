import re

def gym_slang(phrase):
    s = {r"(P|p)robably": "\\1rolly",
         r"(I|i) am": "\\1'm",
         r"(I|i)nstagram": "\\1nsta",
         r"(D|d)o not": "\\1on't",
         r"(G|g)oing to": "\\1onna",
         r"(C|c)ombination": "\\1ombo"}
    for k, v in s.items():
        phrase = re.sub(k, v, phrase)
    return phrase
