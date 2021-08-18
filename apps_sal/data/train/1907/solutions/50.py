
class Solution1:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        p = deque([original])
        q = deque([cloned])
        while p and q:
            for _ in range(len(q)):
                node_o = p.popleft()
                node_c = q.popleft()
                if node_o == target:
                    return node_c
                if node_o.left:
                    p.append(node_o.left)
                if node_o.right:
                    p.append(node_o.right)
                if node_c.left:
                    q.append(node_c.left)
                if node_c.right:
                    q.append(node_c.right)
        return None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def preorder(root: TreeNode):
            yield root
            if root.left:
                yield from preorder(root.left)
            if root.right:
                yield from preorder(root.right)

        for p, q in zip(preorder(original), preorder(cloned)):
            if p == target:
                return q
        return None
