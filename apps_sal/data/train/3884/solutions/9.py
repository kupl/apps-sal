import re


def gym_slang(phrase):
    s = {'(P|p)robably': '\\1rolly', '(I|i) am': "\\1'm", '(I|i)nstagram': '\\1nsta', '(D|d)o not': "\\1on't", '(G|g)oing to': '\\1onna', '(C|c)ombination': '\\1ombo'}
    for (k, v) in s.items():
        phrase = re.sub(k, v, phrase)
    return phrase
