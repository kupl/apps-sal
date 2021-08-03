class Solution:

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        maxlen = 1
        start = 1
        end = 1
        tlen = 1
        l = [[root, 1]]

        while tlen:
            llen = tlen
            tlen = 0
            while llen:
                cur = l.pop(0)
                llen -= 1
                if cur[0]:
                    l.append([cur[0].left, 2 * cur[1] - 1])
                    l.append([cur[0].right, 2 * cur[1]])
                    tlen += 2

            if len(l) > 0:
                for item in reversed(l):
                    if item[0]:
                        end = item[1]
                        break
                if end != item[1]:
                    return maxlen

                for item in l:
                    if item[0]:
                        start = item[1]
                        break

                end = end - start + 1
                if(end > maxlen):
                    maxlen = end

                start = end = -1

        return maxlen
