
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.search(cloned, target)

    def search(self, head, target):
        if head is None:
            return None
        if head.val == target.val:
            return head
        else:
            left_node = self.search(head.left, target)
            if left_node is None:
                return self.search(head.right, target)
            else:
                return left_node
