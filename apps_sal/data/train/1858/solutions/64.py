# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    # list1=[]

    def __init__(self, root: TreeNode):
        root.val = 0
        self.list1 = []
        self.helper(root)

    def helper(self, root):
        if not root:
            return
        self.list1.append(root.val)
        if root.left:
            root.left.val = 2 * root.val + 1

        if root.right:
            root.right.val = 2 * root.val + 2
           # print(self.list1)
        self.helper(root.left)
        self.helper(root.right)
   # print(\"list1\",list1)

    def find(self, target: int) -> bool:
        if target in self.list1:
            return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
