def is_anagram(test: str, original: str) -> bool:
    """ Check if the two given parameters create an anagram. """
    return all([all([_ in original.lower() for _ in test.lower()]), len(test) == len(original)])
