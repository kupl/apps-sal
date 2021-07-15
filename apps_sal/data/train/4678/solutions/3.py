def find_the_missing_tree(trees):
    return -sum(trees) % sum(set(trees))
