from collections import deque
from math import log2, floor


def split_tree(a):
    top_position = 0
    number_of_elements = len(a)
    number_of_layers = floor(log2(number_of_elements)) + 1
    top_size = 2 ** (number_of_layers - 1) - 1
    lowest_level_count = number_of_elements - top_size
    if lowest_level_count >= 2 ** (number_of_layers - 2):
        top_position = int(2**(number_of_layers - 1)) - 1
    else:
        top_position = - (top_size - 1) // 2 - 1
    return a[top_position], a[:top_position], a[top_position + 1:]


def complete_binary_tree(a):
    res = []
    tree_queue = deque()
    tree_queue.append(a)
    while tree_queue:
        tree = tree_queue.popleft()
        if tree:
            (root, left, right) = split_tree(tree)
            res.append(root)
            tree_queue.append(left)
            tree_queue.append(right)
    return res
