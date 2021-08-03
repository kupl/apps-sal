from re import sub

dict = {"([pP]ro)bably": r"\1lly",
        "([iI]) am": r"\1'm",
        "([iI]nsta)gram": r"\1",
        "([dD]o) not": r"\1n't",
        "([gG]o)ing to": r"\1nna",
        "([cC]omb)ination": r"\1o"}


def gym_slang(phrase):
    for k, v in dict.items():
        phrase = sub(k, v, phrase)
    return phrase
