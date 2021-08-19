class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.numDict = defaultdict(list)
        for (i, num) in enumerate(arr):
            self.numDict[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        leftCandi = right - left + 1
        iNow = right
        visited = set()
        while leftCandi >= threshold:
            if self.arr[iNow] not in visited:
                visited.add(self.arr[iNow])
                numOfINow = self.count(iNow, left)
                if numOfINow >= threshold:
                    return self.arr[iNow]
                else:
                    leftCandi -= numOfINow
            iNow -= 1
        return -1

    def count(self, i0, left):
        num = self.arr[i0]
        listLen = len(self.numDict[num])
        l = 0
        r = listLen - 1
        if i0 == self.numDict[num][r]:
            right = r
        elif i0 == self.numDict[num][l]:
            right = l
        else:
            while r > l:
                m = (r + l) // 2
                if self.numDict[num][m] < i0:
                    l = m + 1
                elif self.numDict[num][m] > i0:
                    r = m
                else:
                    l = m
                    r = l - 1
            right = l
        l = 0
        r = right
        if left <= self.numDict[num][l]:
            return right + 1
        if left == self.numDict[num][r]:
            return 1
        while r > l:
            m = (r + l) // 2
            if self.numDict[num][m] < left:
                l = m + 1
            else:
                r = m
        return right - l + 1
