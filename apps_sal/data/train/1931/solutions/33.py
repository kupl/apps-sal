class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        paths = []

        def dfs(root, arr):
            arr1 = arr + [str(root.val)]
            if root.left:
                dfs(root.left, arr1)
            if root.right:
                dfs(root.right, arr1)
            if not root.left and not root.right:
                paths.append(arr1)
        dfs(root, [])
        target = []
        while head:
            target.append(str(head.val))
            head = head.next
        tar = '
        for path in paths:
            if tar in '
            return True
        return False
