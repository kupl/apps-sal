from collections import Counter
palindrome_rearranging=lambda s:len(list(filter(lambda x:x&1,Counter(s).values())))<2
