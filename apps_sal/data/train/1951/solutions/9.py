class Solution:

    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        self.arr = []

        def inorder(root):
            if root:
                inorder(root.left)
                self.arr.append(root.val)
                inorder(root.right)

        def solve(nums):
            if len(nums):
                mx = nums.index(max(nums))
                root = TreeNode(nums[mx])
                root.left = solve(nums[:mx])
                root.right = solve(nums[mx + 1:])
                return root
        inorder(root)
        self.arr.append(val)
        return solve(self.arr)
