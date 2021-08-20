def max_match(sentence: str):
    if not sentence:
        return []
    (word, i) = next(filter(lambda w: w[0] in VALID_WORDS, ((sentence[:i], i) for i in range(len(sentence) + 1, 1, -1))), (sentence[0], 1))
    return [word] + max_match(sentence[i:])
