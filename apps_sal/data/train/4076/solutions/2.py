def get_count(words=None):
    ret = {"vowels": 0, "consonants": 0}
    if words and isinstance(words, str):
        for char in words.lower():
            if char in 'aeiouy':
                ret["vowels"] += 1
            elif char.isalpha():
                ret["consonants"] += 1
    return ret
