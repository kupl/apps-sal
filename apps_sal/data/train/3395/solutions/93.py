import re


def remove_duplicate_words(s):
    result = []
    s_l = s.split(' ')

    for x in s_l:
        if x not in result:
            result.append(x)

    result = " ".join(result)
    return result
