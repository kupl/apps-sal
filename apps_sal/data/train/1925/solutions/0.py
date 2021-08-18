class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        vals = deque(preorder)

        def build(min_val, max_val):
            if vals and min_val < vals[0] < max_val:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(min_val, val)
                node.right = build(val, max_val)

                return node

        return build(float('-inf'), float('inf'))
