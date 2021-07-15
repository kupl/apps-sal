def check_DNA(s1, s2):
    s2 = s2[::-1].translate(str.maketrans('ATCG','TAGC'))
    return s1 in s2 or s2 in s1
