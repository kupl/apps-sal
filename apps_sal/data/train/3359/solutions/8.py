from string import ascii_uppercase as a


def title_to_number(title):
    return sum(((a.index(x) + 1) * 26 ** i for (i, x) in enumerate(title[::-1])))
