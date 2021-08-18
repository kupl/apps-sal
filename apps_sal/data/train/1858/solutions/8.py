
def get_path(n: int) -> List[int]:

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
