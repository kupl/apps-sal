from collections import Counter

def find_the_missing_tree(trees):
    return min(Counter(trees).most_common(), key=lambda x: x[1])[0]
