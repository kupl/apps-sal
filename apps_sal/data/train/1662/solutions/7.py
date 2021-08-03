from itertools import chain


def tree_by_levels(node):
    tree = [node]
    temp = [t.value for t in tree if t]
    while tree:
        tree = list(chain(*[[t.left, t.right] for t in tree if t]))
        temp += [t.value for t in tree if t]
    return temp
