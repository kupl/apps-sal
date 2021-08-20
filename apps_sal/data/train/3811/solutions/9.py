def largest_sum(s):
    return max((sum(map(int, c)) for c in s.split('0')))
