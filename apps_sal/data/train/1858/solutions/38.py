class FindElements:

    def __init__(self, root: TreeNode):
        self.l = [0]
        self.root = root
        self.root.val = 0
        d = deque()
        d.append(root)
        while d:
            x = d.popleft()
            if x.left:
                x.left.val = x.val * 2 + 1
                d.append(x.left)
                self.l.append(x.left.val)
            if x.right:
                x.right.val = x.val * 2 + 2
                d.append(x.right)
                self.l.append(x.right.val)

    def find(self, target: int) -> bool:
        return target in self.l
