def vowel_indices(word):
    out=[]
    for i,s in enumerate(word):
        if s.lower() in "aeiouy":
            out.append(i+1)
    return out
