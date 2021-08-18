class FindElements:

    def __init__(self, root: TreeNode):
        self.r = root

        def helper(node, value):
            node.val = value
            if node.left:
                helper(node.left, value * 2 + 1)
            if node.right:
                helper(node.right, value * 2 + 2)
        helper(root, 0)

    def find(self, target: int) -> bool:
        path = target
        stack = []
        while path:
            stack.append(path)
            if path % 2 == 0:
                path -= 2
                if path != 0:
                    path //= 2
            else:
                path -= 1
                if path != 0:
                    path //= 2
        stack.append(0)

        def finder(s, root):

            if not s:
                return True
            if not root:
                return False
            value = s.pop()
            if root.val == value:
                if s:
                    if s[-1] % 2 == 0:
                        return finder(s, root.right)
                    else:
                        return finder(s, root.left)
                else:
                    return True
            else:
                return False
        return finder(stack, self.r)
