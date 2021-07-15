def grabscrab(word, possible_words):
    srch = sorted(word)
    ans = [e for e in possible_words if sorted(e) == srch]
    return ans
