class Tree(object):
    value = summ = None
    left = right = None

    def __init__(self, value):
        self.value = value


def iter_pairs(level):
    it = iter(level)
    a, b = Tree(next(it)), Tree(next(it))
    while b.value is not None:
        yield a, b
        a, b = b, Tree(next(it, None))


def build_tree(pyramid):
    it = iter(pyramid)
    root = Tree(next(iter(next(it))))
    prev_level = iter([root])
    for level in it:
        tree_level = []
        parent = next(prev_level)

        for left_tree, right_tree in iter_pairs(level):
            tree_level.append(left_tree)

            parent.left = left_tree
            parent.right = right_tree
            parent = next(prev_level, None)

        tree_level.append(right_tree)
        prev_level = iter(tree_level)

    return root


def calc_max_sums(root):
    if root is None:
        return 0

    if root.summ is not None:
        return root.summ

    root.summ = root.value + max(calc_max_sums(root.left), calc_max_sums(root.right))
    return root.summ


def find_max_slide(root):
    if root is None:
        return 0

    if not (root.left and root.right):
        return root.value

    if root.left.summ >= root.right.summ:
        return root.value + find_max_slide(root.left)

    if root.left.summ < root.right.summ:
        return root.value + find_max_slide(root.right)


def longest_slide_down(pyramid):
    tree = build_tree(pyramid)
    calc_max_sums(tree)
    return find_max_slide(tree)
