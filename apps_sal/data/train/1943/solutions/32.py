class Solution:
    def overlap(self, lst):
        lst.sort(key=lambda x: x[0])
        if lst[0][1] >= lst[1][0]:
            return True
        return False

    def add_data(self, start_a, end_a, start_b, end_b, res):
        if self.overlap([(start_a, end_a), (start_b, end_b)]):
            start, end = max(start_a, start_b), min(end_a, end_b)
            if (start, end) not in res:
                res.append((start, end))
        return res

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        if not A or not B:
            return []

        start_a, end_a = A.pop(0)
        start_b, end_b = B.pop(0)
        res = []

        while A and B:
            res = self.add_data(start_a, end_a, start_b, end_b, res)
            if end_a < end_b:
                start_a, end_a = A.pop(0)
            else:
                start_b, end_b = B.pop(0)

        while A:
            res = self.add_data(start_a, end_a, start_b, end_b, res)
            start_a, end_a = A.pop(0)

        while B:
            res = self.add_data(start_a, end_a, start_b, end_b, res)
            start_b, end_b = B.pop(0)

        res = self.add_data(start_a, end_a, start_b, end_b, res)

        return res
