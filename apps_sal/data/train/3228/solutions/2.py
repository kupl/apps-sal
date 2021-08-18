def word_pattern(pattern, string):
    match = {}

    if len(pattern) != len(string.split()):
        return False

    for c, word in zip(pattern, string.split()):
        if c not in match:
            if word in list(match.values()):
                return False

            match[c] = word

        if match[c] != word:
            return False

    return True
