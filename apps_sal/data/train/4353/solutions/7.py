def could_be(a, b, s=set):
    return s() < s(b.split()) <= s(a.split()) > s()
