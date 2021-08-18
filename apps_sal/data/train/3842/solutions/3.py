def word_wrap(text, limit):
    text = text.split(" ")
    res = ""
    c = 0
    i = 0
    while i < len(text):
        curr_word = text[i]
        if len(curr_word) <= (limit - c):
            add_ws = len(curr_word) < (limit - c) and i < len(text) - 1
            res += curr_word + (" " if add_ws else "")
            c += len(curr_word) + (1 if add_ws else 0)
            i += 1
        elif len(curr_word) > limit:
            res += curr_word[:(limit - c)] + "\n"
            text[i] = curr_word[(limit - c):]
            c = 0
        else:
            res = res.rstrip()
            res += "\n"
            c = 0
    return res
