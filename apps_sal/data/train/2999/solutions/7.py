def hex_word_sum(s):
    total = 0

    for word in s.replace("O", "0").replace("S", "5").split():
        try:
            total += int(word, 16)
        except ValueError:
            pass

    return total
