def compare(s1, s2):
    return (sum(map(ord, s1.upper())) if type(s1) is str and s1.isalpha() else 0) == (sum(map(ord, s2.upper())) if type(s2) is str and s2.isalpha() else 0)

