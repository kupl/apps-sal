import re


def gym_slang(phrase):
    phrase = re.sub('([pP])robably', '\\1rolly', phrase)
    phrase = re.sub('([iI]) am', "\\1'm", phrase)
    phrase = re.sub('([iI])nstagram', '\\1nsta', phrase)
    phrase = re.sub('([dD])o not', "\\1on't", phrase)
    phrase = re.sub('([gG])oing to', '\\1onna', phrase)
    phrase = re.sub('([cC])ombination', '\\1ombo', phrase)
    return phrase
