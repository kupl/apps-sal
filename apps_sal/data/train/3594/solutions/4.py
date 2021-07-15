def is_isogram(word):
    if type(word) is str:
        if word is not None:
            w = ''.join(i.lower() for i in word if ord(i.lower()) in range(97,123) or ord(i.lower()) in range(48,58))
            if len(w) > 0:
                if len(w) % len(set(w)) == 0:
                    return True
    return False

