from re import sub


def word_count(s):
    alpha = sub("(^|\s)(a|the|on|at|of|in|as)(?=(\s|$))", ' ', sub("[^a-z]", ' ', s.lower().replace('æ', 'ae')))
    return len(alpha.split())
