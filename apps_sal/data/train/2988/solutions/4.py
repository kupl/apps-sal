def reverse_and_combine_text(stg):
    if not " " in stg:
        return stg
    words = [word[::-1] for word in stg.split()] + [""]
    result = " ".join(f"{w1}{w2}" for w1, w2 in zip(words[::2], words[1::2]))
    return reverse_and_combine_text(result)       
