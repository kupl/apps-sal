class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = collections.deque()
        q.append([original, cloned])
        while q:
            (ori, cop) = q.popleft()
            if ori == target:
                return cop
            else:
                if ori.left:
                    q.append([ori.left, cop.left])
                if ori.right:
                    q.append([ori.right, cop.right])
