from collections import Counter
def get_strings(city):
    l = []
    d = Counter(city.lower())
    for c,n in d.items():
        if c == " ":
            continue
        l.append(c+":"+"*"*n)
    return ",".join(l)
