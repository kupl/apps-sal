from collections import Counter, defaultdict
def get_char_count(s):
    d = defaultdict(list)
    c = Counter(sorted(s.lower()))
    for i,j in c.items():
        if i.isalnum() : d[j].append(i)
    return dict(sorted(d.items())[::-1])
