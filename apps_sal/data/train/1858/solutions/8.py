# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def get_path(n: int) -> List[int]:
    # x = 2*(2*(2*(2*0 + a) + b) + c) + d
    # x = 2*(2*(2*a + b) + c) + d
    # x = 2*(4*a + 2*b + c) + d
    # x = 8*a + 4*b + 2*c + d

    # x % 2 = 0 + 0 + 0 + (d%2)
    # if d == 1 -> d%2 = 1
    # if d == 2 -> d%2 = 0

    result = []
    while n > 0:
        if n % 2 == 0:
            digit = 2
        else:
            digit = 1

        result.append(digit)
        n -= digit
        n //= 2
    return result


def find(root: TreeNode, path: List[int]) -> bool:
    if root is None:
        return False

    if not path:
        return True

    direction = path.pop()
    if direction == 1:
        if root.left:
            root.left.val = 2 * root.val + 1
        return find(root.left, path)
    elif direction == 2:
        if root.right:
            root.right.val = 2 * root.val + 2
        return find(root.right, path)

    return False


class FindElements:
    def __init__(self, root: TreeNode):
        root.val = 0
        self.tree = root

    def find(self, target: int) -> bool:
        p = get_path(target)
        return find(self.tree, p)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
