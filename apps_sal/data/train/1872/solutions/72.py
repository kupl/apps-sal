class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        stack = [root]
        record = {0: root.val}
        length = 0
        while len(stack) > 0:
            tmp = []
            val = 0
            length += 1
            for s in stack:
                if s.left:
                    tmp.append(s.left)
                    val += s.left.val
                if s.right:
                    tmp.append(s.right)
                    val += s.right.val
            record[length] = val
            stack = tmp[:]
        max_val = max(list(record.values()))
        for i in range(length):
            if record[i] == max_val:
                return i + 1
