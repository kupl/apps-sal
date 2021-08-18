class FindElements:

    def __init__(self, root: TreeNode):

        self.root = root
        self.container = set()

        def helper(root, val):

            if not root:
                return

            root.val = val
            helper(root.left, root.val * 2 + 1)
            helper(root.right, root.val * 2 + 2)

        helper(self.root, 0)
        return

    def find(self, target: int) -> bool:

        def findpath(target):
            path = [target]
            while target:
                diff = 1 if target % 2 else 2
                target = int((target - diff) / 2)
                path.append(target)

            return path[::-1]

        def trav(node, depth, path):
            if depth > len(path):
                return False
            else:
                if not node:
                    return False
                if node.val == path[-1]:
                    return True
                if node.val == path[depth]:
                    res = trav(node.left, depth + 1, path) or trav(node.right, depth + 1, path)
                    return res
            return False

        path = findpath(target)
        return trav(self.root, 0, path)
