class Solution:

    def compare(self, x, y):
        x_ = set(x)
        for i in x_:
            if x.count(i) != y.count(i):
                return False
        return True

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return self.compare(target, arr)
