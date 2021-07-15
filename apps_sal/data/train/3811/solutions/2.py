def largest_sum(s):
    return max(sum(int(i) for i in j) for j in s.split('0'))
