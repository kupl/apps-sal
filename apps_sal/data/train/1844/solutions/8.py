class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def cv2mnt(t):
            h, m = t.split(':')
            mnt = int(h) * 60 + int(m)
            return mnt
        lst = [0 for i in range(1440)]
        for t in timePoints:
            mnt = cv2mnt(t)
            if lst[mnt] == 1:
                return 0
            else:
                lst[mnt] = 1
        beg = 0
        stk = [i for i, n in enumerate(lst) if n == 1]
        stk.append(stk[0] + 1440)
        res = 1439
        for i in range(len(stk) - 1):
            dif = abs(stk[i] - stk[i + 1])
            dif_ = min(1440 - dif, dif)
            res = min(res, dif_)
            if res == 1:
                return 1
        return res
