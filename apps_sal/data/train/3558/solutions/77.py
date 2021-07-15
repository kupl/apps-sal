def capitalize_word(word):
    return "".join(word[char].upper() if char == 0 else word[char] for char in range(0, len(word)) )
