import re


def bucket_of(said):
    pattern1 = r"water|wet|wash"
    pattern2 = r"slime|i don't know"
    result1 = re.search(pattern1, said, re.I)
    result2 = re.search(pattern2, said, re.I)
    if result1 and result2:
        return "sludge"
    elif result1:
        return "water"
    elif result2:
        return "slime"
    else:
        return "air"
