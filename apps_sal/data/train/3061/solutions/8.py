from collections import Counter
most_frequent_item_count=lambda c: Counter(c).most_common(1)[0][1] if c else 0
