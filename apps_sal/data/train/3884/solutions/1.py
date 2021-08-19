from re import sub
dict = {'([pP]ro)bably': '\\1lly', '([iI]) am': "\\1'm", '([iI]nsta)gram': '\\1', '([dD]o) not': "\\1n't", '([gG]o)ing to': '\\1nna', '([cC]omb)ination': '\\1o'}


def gym_slang(phrase):
    for (k, v) in dict.items():
        phrase = sub(k, v, phrase)
    return phrase
