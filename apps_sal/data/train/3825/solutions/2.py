from re import sub, I


def filter_words(phrase):
    return sub('(bad|mean|ugly|horrible|hideous)', 'awesome', phrase, flags=I)
