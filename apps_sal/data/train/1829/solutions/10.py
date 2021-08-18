class Solution:
    def __init__(self):
        self.total_count = 0

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, [])

    def goodNodesHelper(self, root, max_first_stack):
        if not root:
            return
        elif max_first_stack == []:
            max_first_stack.append(root.val)
            self.total_count += 1

        elif max_first_stack[0] <= root.val:
            max_first_stack = [root.val] + max_first_stack
            self.total_count += 1
        else:
            max_first_stack = max_first_stack + [root.val]
        self.goodNodesHelper(root.left, max_first_stack)
        self.goodNodesHelper(root.right, max_first_stack)
        return self.total_count
