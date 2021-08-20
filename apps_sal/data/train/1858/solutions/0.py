class FindElements:

    def __init__(self, root: TreeNode):
        self.dicts = {}
        if root:
            root.val = 0
            stacks = [root]
            self.dicts[0] = 1
            while stacks:
                new_stacks = []
                for element in stacks:
                    if element.left:
                        element.left.val = element.val * 2 + 1
                        new_stacks.append(element.left)
                        self.dicts[element.left.val] = 1
                    if element.right:
                        element.right.val = element.val * 2 + 2
                        new_stacks.append(element.right)
                        self.dicts[element.right.val] = 1
                stacks = new_stacks

    def find(self, target: int) -> bool:
        return target in self.dicts
