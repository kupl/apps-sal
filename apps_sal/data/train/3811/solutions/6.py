def largest_sum(s):
    return max(sum(map(int, list(n))) for n in s.split('0'))
