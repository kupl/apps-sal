def string_to_array(s):
    words = s.split()
    if not words:
        words.insert(0, "")
    return words
