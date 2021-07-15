def palindrome_rearranging(s):
    return [s.count(i)%2 for i in set(s)].count(1) == len(s)%2
