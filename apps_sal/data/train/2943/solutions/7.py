import math


def complete_binary_tree(a):
    if len(a) < 2:
        return a

    root = build(a)
    res = []
    getLevelOrder(root, res)
    return res


class Node:

    def __init__(self, data, left, right):

        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        return f"left = {self.left}, right = {self.right}, data = {self.data}"


def build(a):

    if len(a) == 0:
        return None
    if len(a) == 1:
        return Node(a[0], None, None)

    level = math.log2(len(a))
    level = math.ceil(level) + (1 if int(level) == level else 0)

    if len(a) >= 2 ** (level - 2) * 3 - 1:
        root = 2 ** (level - 1) - 1
    else:
        root = len(a) - 2 ** (level - 2)

    left = build(a[:root])
    right = build(a[root + 1:])
    return Node(a[root], left, right)


def getLevelOrder(root, res):
    h = height(root)
    for i in range(1, h + 1):
        getGivenLevel(root, i, res)


def getGivenLevel(root, level, res):
    if root is None:
        return
    if level == 1:
        res.append(root.data)
    elif level > 1:
        getGivenLevel(root.left, level - 1, res)
        getGivenLevel(root.right, level - 1, res)


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
