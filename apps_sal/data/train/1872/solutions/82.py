class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        import collections
        queue = collections.deque([root])
        maxx = root.val
        ans = 0
        level = 1
        while queue:
            summ = 0
            for i in range(len(queue)):
                n = queue.popleft()
                if not n:
                    continue
                summ += n.val
                queue.append(n.left)
                queue.append(n.right)
            if summ > maxx:
                ans = level
                maxx = summ
            level += 1
        return ans
