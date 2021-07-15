def hex_word_sum(stg):
    valid_chars = set("05ABCDEF")
    stg = stg.replace("S", "5").replace("O", "0")
    valid_words = (word for word in stg.split() if not (set(word) - valid_chars))
    return sum(int(word, 16) for word in valid_words)

