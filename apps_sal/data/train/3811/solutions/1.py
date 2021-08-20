def largest_sum(s):
    return max((sum(map(int, e)) for e in s.split('0')))
