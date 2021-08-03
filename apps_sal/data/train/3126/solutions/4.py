from collections import Counter
def palindrome_rearranging(s): return len(list(filter(lambda x: x & 1, Counter(s).values()))) < 2
