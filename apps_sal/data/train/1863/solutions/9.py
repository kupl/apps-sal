class Solution:

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        from queue import Queue
        Q = Queue()
        dic = {}
        horizontal_distance = 0
        level = 1
        Q.put([root, horizontal_distance, level])
        dic[horizontal_distance] = dic.get(horizontal_distance, []) + [[root.val, level]]
        while not Q.empty():
            p = Q.get()
            currentRoot = p[0]
            currentHD = p[1]
            currentLevel = p[2]
            if currentRoot.left:
                Q.put([currentRoot.left, currentHD - 1, currentLevel + 1])
                dic.setdefault(currentHD - 1, []).append([currentRoot.left.val, currentLevel + 1])
            if currentRoot.right:
                Q.put([currentRoot.right, currentHD + 1, currentLevel + 1])
                dic.setdefault(currentHD + 1, []).append([currentRoot.right.val, currentLevel + 1])
        del currentRoot, currentHD, currentLevel, p, Q
        templist = []
        from operator import itemgetter
        for key in sorted(dic.keys()):
            templist.append((i[0] for i in sorted(dic[key], key=itemgetter(1, 0))))
        return templist
