def find_the_missing_tree(trees):
    return min(trees, key=lambda n: trees.count(n))
