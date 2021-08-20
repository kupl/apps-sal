def title_to_number(title):
    return sum(((ord(char) - 64) * 26 ** i for (i, char) in enumerate(title[::-1])))
