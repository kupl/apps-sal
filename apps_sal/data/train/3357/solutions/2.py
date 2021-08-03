from collections import Counter
def find_dup(xs): return Counter(xs).most_common(1)[0][0]
