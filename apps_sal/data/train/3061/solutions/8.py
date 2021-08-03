from collections import Counter
def most_frequent_item_count(c): return Counter(c).most_common(1)[0][1] if c else 0
