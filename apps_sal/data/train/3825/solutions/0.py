import re
def filter_words(phrase):
    return re.sub("(bad|mean|ugly|horrible|hideous)","awesome",
        phrase,flags=re.IGNORECASE)
