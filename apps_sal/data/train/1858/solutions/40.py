class FindElements:

    def rebuild(self, root: TreeNode):
        queue = []
        root.val = 0
        queue.append(root)
        while queue:
            new = queue.pop(0)
            if new.left:
                new.left.val = 2 * new.val + 1
                self.collection.append(new.left.val)
                queue.append(new.left)
            if new.right:
                new.right.val = 2 * new.val + 2
                self.collection.append(new.right.val)
                queue.append(new.right)

    def __init__(self, root: TreeNode):
        self.copy = root
        self.collection = [0]
        self.rebuild(self.copy)

    def find(self, target: int) -> bool:
        return target in self.collection
