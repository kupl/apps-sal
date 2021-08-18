
class Solution:
    def __init__(self):
        self.clone: TreeNode = None

    def find_possible_target(self, cloned: TreeNode, target: TreeNode):
        if not cloned:
            return None
        if cloned.val == target.val:
            return cloned

        possible_target = self.find_possible_target(cloned.left, target)
        if possible_target:
            return possible_target

        return self.find_possible_target(cloned.right, target)

    def are_they_copy(self, cloned: TreeNode, target: TreeNode) -> bool:
        if not cloned and not target:
            return True
        if cloned and not target:
            return False
        if not cloned and target:
            return False

        if not cloned.val == target.val:
            return False

        if not self.are_they_copy(cloned.left, target.left):
            return False

        return self.are_they_copy(cloned.right, target.right)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        if original is None or original == target:
            return cloned

        possible_target = self.find_possible_target(cloned, target)
        return possible_target
