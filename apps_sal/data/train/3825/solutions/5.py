from re import sub


def filter_words(phrase):
    return sub(r"(bad|mean|ugly|horrible|hideous)(?i)", "awesome", phrase)
