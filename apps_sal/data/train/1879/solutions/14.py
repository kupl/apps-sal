import queue


class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = queue.deque()
        q.append(root)
        ans = 0
        while q:
            ans = 0
            for _ in range(len(q)):
                cur_node = q.popleft()
                ans += cur_node.val
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
        return ans
