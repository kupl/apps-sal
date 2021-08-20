def first(gen):
    for elem in gen:
        return elem


def walk(original, cloned, target):
    if not original:
        return
    elif original is target:
        yield cloned
    else:
        yield from walk(original.left, cloned.left, target)
        yield from walk(original.right, cloned.right, target)


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return first(walk(original, cloned, target))
