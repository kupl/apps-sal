def largest_sum(s):
    return max(sum(map(int, i)) for i in s.split("0"))
