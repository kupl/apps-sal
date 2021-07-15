validate_word = lambda w: len(set(w.lower().count(e) for e in set(w.lower())))==1
