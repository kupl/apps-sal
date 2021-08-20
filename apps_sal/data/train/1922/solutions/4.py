class Solution:

    @lru_cache(None)
    def helper(self, node, covered, camera):
        if node == None:
            return 0
        if camera:
            return 1 + self.helper(node.left, True, False) + self.helper(node.right, True, False)
        if covered:
            cam_on = 1 + self.helper(node.left, True, False) + self.helper(node.right, True, False)
            cam_off = self.helper(node.left, False, False) + self.helper(node.right, False, False)
            return min(cam_on, cam_off)
        cam_on = 1 + self.helper(node.left, True, False) + self.helper(node.right, True, False)
        cam_on_left = self.helper(node.left, False, True) + self.helper(node.right, False, False) if node.left != None else inf
        cam_on_right = self.helper(node.left, False, False) + self.helper(node.right, False, True) if node.right != None else inf
        return min(cam_on, cam_on_left, cam_on_right)

    def minCameraCover(self, root: TreeNode) -> int:
        return min(self.helper(root, False, True), self.helper(root, False, False))
