def to_freud(sentence):
    import re
    return re.sub('\S+', 'sex', sentence)
