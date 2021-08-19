class Solution:
    def minCameraCover(self, root):
        self._res = 0
        if self._dfs(root) == 0:
            self._res += 1
        return self._res

    # 0表示这个点没有被cover
    # 1表示这个点被cover了，但是没有camera
    # 2表示这个点有camera
    def _dfs(self, node):
        # 空点我们也认为被cover了
        # 但是没有camera
        if not node:
            return 1

        left = self._dfs(node.left)
        right = self._dfs(node.right)

        # 如果左节点或者右节点中有cover不住的
        # 需要在node上加camera了
        if left == 0 or right == 0:
            self._res += 1
            return 2
        elif left == 2 or right == 2:
            return 1
        # 此时左节点和右节点肯定都是1
        # 表示左右孩子都被cover住了
        # 我们直接退出，在主函数里面处理这个node就好了
        else:
            return 0
