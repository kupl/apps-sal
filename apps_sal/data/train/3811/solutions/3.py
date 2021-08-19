def largest_sum(s):
    return max((sum((int(x) for x in n)) for n in s.split('0')))
