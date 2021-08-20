import math


class BST:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def complete_binary_tree(arr):
    tree = bst_from_arr(arr)
    depth = math.floor(math.log(len(arr), 2))
    output = []
    for i in range(depth + 1):
        output += breadth_first_arr(tree, i)
    return output


def breadth_first_arr(tree, level):
    out = []
    if tree is None:
        return
    if level == 0:
        out.append(tree.value)
    elif level > 0:
        if tree.left:
            out += breadth_first_arr(tree.left, level - 1)
        if tree.right:
            out += breadth_first_arr(tree.right, level - 1)
    return out


def bst_from_arr(arr):
    if len(arr) > 1:
        root_index = get_root_index(arr)
        tree = BST(arr[root_index])
    else:
        return BST(arr[0])
    if len(arr[:root_index]) > 1:
        tree.left = bst_from_arr(arr[:root_index])
    if len(arr[:root_index]) == 1:
        tree.left = BST(arr[0])
    if len(arr[root_index + 1:]) > 1:
        tree.right = bst_from_arr(arr[root_index + 1:])
    if len(arr[root_index + 1:]) == 1:
        tree.right = BST(arr[-1])
    return tree


def get_root_index(arr):
    left_subtree = 0
    levels = math.floor(math.log(len(arr), 2))
    for i in range(0, levels):
        if not i == levels - 1:
            left_subtree += 2 ** i
        else:
            left_subtree += min(int(2 ** levels / 2), len(arr) - (2 ** levels - 1))
    return left_subtree
