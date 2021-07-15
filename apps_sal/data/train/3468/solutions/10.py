from collections import Counter
scramble = lambda s1, s2: not Counter(s2) - Counter(s1)
