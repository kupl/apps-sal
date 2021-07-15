def max_match(sentence):
    found = []
    while sentence:
        for i in range(len(sentence), 0, -1):
            chunk = sentence[:i]
            if chunk in VALID_WORDS:
                break
        found.append(chunk)
        sentence = sentence[i:]
    return found
