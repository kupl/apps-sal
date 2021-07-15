from string import ascii_lowercase as alphabet

def same_encryption(s1, s2):
    sum_s1 = len(s1[1:-1])
    sum_s2 = len(s2[1:-1])
    while len(str(sum_s1)) > 1:
        sum_s1 = sum(map(int, str(sum_s1)))
    while len(str(sum_s2)) > 1:
        sum_s2 = sum(map(int, str(sum_s2)))
    return '{}{}{}'.format(s1[0], sum_s1, s1[-1]) == '{}{}{}'.format(s2[0], sum_s2, s2[-1])
