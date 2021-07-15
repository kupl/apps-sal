from collections import Counter

def find_the_missing_tree(trees):
    counter = Counter(trees)
    return min(counter.keys(), key=counter.get)
