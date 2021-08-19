def capitalize_word(word):
    # return word.title()
    return "".join(char.upper() if idx == 0 else char for idx, char in enumerate(word))
