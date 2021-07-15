def kontti(s):
    result = []
    for w in s.split():
        i = next((i for i,c in enumerate(w, 1) if c in "aeiouyAEIOUY"), None)
        result.append(w if i is None else f"ko{w[i:]}-{w[:i]}ntti")
    return ' '.join(result)
