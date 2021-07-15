def position(alphabet):
    import string
    characters = {char: str(idx) for idx, char in enumerate(string.ascii_lowercase, 1)}
    return f"Position of alphabet: {characters[alphabet]}"

