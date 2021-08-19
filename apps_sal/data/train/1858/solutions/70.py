class FindElements:

    def __init__(self, root: TreeNode):
        stack = [[root.left, 1, 0], [root.right, 2, 0]]
        self.ans = [0]
        while stack:
            x = stack.pop(0)
            if x[0] is not None:
                val = x[2] * 2 + x[1]
                self.ans.append(val)
                stack.append([x[0].left, 1, val])
                stack.append([x[0].right, 2, val])
        print(self.ans)

    def find(self, target: int) -> bool:
        return target in self.ans
