from string import punctuation

t = str.maketrans("", "", punctuation)

def pseudo_sort(s):
    a = s.translate(t).split()
    b = sorted(x for x in a if x[0].islower())
    c = sorted((x for x in a if x[0].isupper()), reverse=True)
    return " ".join(b + c)
