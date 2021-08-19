# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root

        def recover(head, val):
            # if not head 比 if head is None 快
            # 在 TreeNode 下两者等价，但注意后者更规范
            # x = []
            # if not x      -- True
            # if x is None  -- False
            if not head:
                return
            head.val = val
            recover(head.left, val * 2 + 1)
            recover(head.right, val * 2 + 2)
        recover(root, 0)

    def find(self, target: int) -> bool:
        steps = bin(target + 1)[3:]
        head = self.root
        for s in steps:
            if not head:
                return False
            if s == '0':
                head = head.left
            else:
                head = head.right
        return head and head.val == target


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
