import heapq


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        add_index = [tup + [idx] for (tup, idx) in zip(points, list(range(len(points))))]
        print(add_index)
        sorted_by_second = sorted(add_index, key=lambda tup: sqrt(tup[1] ** 2 + tup[0] ** 2))
        res = []
        for i in range(K):
            res += [sorted_by_second[i][:2]]
        return res
