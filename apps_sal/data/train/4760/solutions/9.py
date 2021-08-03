from operator import gt, lt


def max_child(root):
    max_val = root.value
    if root.left is not None:
        max_left = max_child(root.left)
        max_val = max(max_val, max_left)
    if root.right is not None:
        max_right = max_child(root.right)
        max_val = max(max_val, max_right)
    return max_val


def min_child(root):
    min_val = root.value
    if root.left is not None:
        min_left = min_child(root.left)
        min_val = min(min_val, min_left)
    if root.right is not None:
        min_right = min_child(root.right)
        min_val = min(min_val, min_right)
    return min_val


comparator_mapper = {
    gt: max_child,
    lt: min_child
}


class T:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(node):
    if node is None:
        return True
    if node.left is not None and node.left.value > node.value or node.right is not None and node.right.value < node.value:
        return validate(node, lt, gt)

    return validate(node, gt, lt)


def validate(root, left_tree_compare, right_tree_compare):
    if root is None:
        return True

    return (left_tree_compare(root.value,
                              comparator_mapper[left_tree_compare](root.left)) if root.left is not None else True) and (
        right_tree_compare(root.value, comparator_mapper[right_tree_compare](
            root.right)) if root.right is not None else True) and validate(
        root.left, left_tree_compare, right_tree_compare) and validate(root.right, left_tree_compare,
                                                                       right_tree_compare)
