def compare(s1, s2):
    s1_sum = 0
    s2_sum = 0

    if type(s1) is str and s1.isalpha():
        s1 = s1.upper()
        s1_sum = sum(list(map(ord, s1)))

    if type(s2) is str and s2.isalpha():
        s2 = s2.upper()
        s2_sum = sum(list(map(ord, s2)))

    return s1_sum == s2_sum
