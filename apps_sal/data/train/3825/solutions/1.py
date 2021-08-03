from re import sub


def filter_words(phrase):
    return sub("(?i)(bad|mean|ugly|horrible|hideous)", "awesome", phrase)
