def compound_array(a, b):
    return [l[i] for i in range(max(len(a), len(b))) for l in (a, b) if i < len(l)]
