def soundex(name):
    consonants_to_digits = {c: str(i)
                            for i, consonants in enumerate("bfpv cgjkqsxz dt l mn r".split(), 1)
                            for cs in consonants
                            for c in cs}

    def soundex_word(word):
        result = word.lower()
        result = (c for i, c in enumerate(result) if i == 0 or c not in "hw")
        result = (consonants_to_digits.get(c, c) for c in result)
        result = uniq(result)
        result = (c for i, c in enumerate(result) if i == 0 or c not in "aeiouy")
        result = "".join(result)
        result = word[0].upper() + result[1:]
        result = format(result, "0<4.4")
        return result
    return " ".join(soundex_word(word) for word in name.split())


def uniq(iterable):
    iterable = iter(iterable)
    previous = next(iterable)
    yield previous
    for elem in iterable:
        if elem != previous:
            yield elem
            previous = elem
