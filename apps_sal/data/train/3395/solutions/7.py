d = {}
remove_duplicate_words = lambda s: " ".join(d.setdefault(w, w) for w in s.split() if w not in d)
