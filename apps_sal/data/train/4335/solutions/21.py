def anagrams(word, words):
    w_buff = []
    w_out = []
    for w_t in words:
        if len(w_t) == len(word):
            w_buff.append(w_t)
    w_w = list(word)
    w_w.sort()
    for w_t in w_buff:
        w_buff_l = list(w_t)
        w_buff_l.sort()
        if w_buff_l == w_w:
            w_out.append(w_t)
    return w_out
