class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = []
        hsh = {}
        from sortedcontainers import SortedList

        for i in range(len(arr)):
            if arr[i] not in hsh:
                hsh[arr[i]] = len(self.arr)
                self.arr.append([arr[i], SortedList()])
            self.arr[hsh[arr[i]]][1].add(i)

        self.arr.sort(key=lambda x: len(x[1]), reverse=True)

    def query(self, left: int, right: int, threshold: int) -> int:

        for i in self.arr:
            if len(i[1]) < threshold:
                return -1

            l = i[1].bisect_left(left)
            r = i[1].bisect_right(right)

            if r - l >= threshold:
                return i[0]

        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
