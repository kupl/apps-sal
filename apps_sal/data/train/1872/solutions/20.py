from collections import defaultdict
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levelSum = defaultdict(int)
        curLevel = 0
        q = [root]
        while q:
            q_length = len(q)
            for i in range(q_length):
                cur = q.pop()
                levelSum[curLevel] += cur.val
                if cur.left: q.insert(0, cur.left)
                if cur.right: q.insert(0, cur.right)
                
            curLevel += 1
            
        maxSumm = max(levelSum.values())
        for l in range(len(levelSum)):
            if levelSum[l] == maxSumm: return l+1
