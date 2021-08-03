def letter_frequency(text):
    d = {}
    for i in text:
        if i.isalpha():
            i = i.lower()
            d[i] = d[i] + 1 if i in d else 1
    return sorted(d.items(), key=lambda k_v: (-k_v[1], k_v[0]))
