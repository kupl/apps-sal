from collections import Counter, defaultdict


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.dic = defaultdict()

    def query(self, left: int, right: int, threshold: int) -> int:
        if (left, right) in self.dic:
            if self.dic[(left, right)][1] >= threshold:
                return self.dic[(left, right)][0]
            else:
                return -1
        sub = self.arr[left:right + 1]
        dic = Counter(sub)
        sum_f = 0
        for ele, freq in list(dic.items()):
            if freq >= threshold:
                self.dic[(left, right)] = (ele, freq)
                return ele
            sum_f += freq
            if sum_f > threshold:
                return -1
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
