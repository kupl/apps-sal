trans = str.maketrans("abdeiknoprtuvwxy", "αβδεικηθρπτμυωχγ")

def gr33k_l33t(string):
    return string.lower().translate(trans)
