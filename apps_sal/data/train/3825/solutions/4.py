def filter_words(s):
    sl = s.lower()
    while any(w in sl for w in ("bad", "mean", "ugly", "horrible", "hideous")):
        for w in ("bad", "mean", "ugly", "horrible", "hideous"):
            if w in sl:
                i = sl.find(w)
                s = s[:i] + 'awesome' + s[i + len(w):]
                sl = s.lower()  # yuk
    print(s)
    return s
