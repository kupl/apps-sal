class Solution:
    def dfs(self, nums, i, tree_node, memo):
        if i >= len(nums):
            return True
        if not tree_node:
            return False

        key = str(i) + ':' + str(id(tree_node))
        if key in memo:
            return memo[key]

        if tree_node.val == nums[i]:
            left = self.dfs(nums, i + 1, tree_node.left, memo)
            right = self.dfs(nums, i + 1, tree_node.right, memo)
            if left or right:
                return True

        left = self.dfs(nums, 0, tree_node.left, memo)
        right = self.dfs(nums, 0, tree_node.right, memo)

        memo[key] = left or right

        return left or right

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False

        memo = {}

        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        return self.dfs(nums, 0, root, memo)
