from collections import Counter
find_dup = lambda xs: Counter(xs).most_common(1)[0][0]
