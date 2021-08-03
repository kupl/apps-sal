def count_string(s):
    if s == '' or s == None:
        return ''
    sum_s = 0
    for i in s.upper():
        if not i.isalpha():
            return ''
        else:
            sum_s += ord(i)
    return sum_s


def compare(s1, s2):
    return count_string(s1) == count_string(s2)
