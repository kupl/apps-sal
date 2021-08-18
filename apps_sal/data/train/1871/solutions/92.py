class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        deque = collections.deque([[root, []]])
        result = 0
        while deque:
            node, anc = deque.popleft()
            max_abs = 0 if not len(anc) else max(abs(node.val - a.val) for a in anc)
            result = max(result, max_abs)
            if node.left:
                deque.append([node.left, anc + [node]])
            if node.right:
                deque.append([node.right, anc + [node]])
        return result
