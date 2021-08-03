# from ACgenerator.Y_Testing import get_code
from _bisect import bisect_left
from collections import Counter


def inversion(iterable):
    \"\"\"
    the number of j s.t (a[i] > a[j]) and (i < j) for each i
    Example:
        inversion([2, 3, 4, 2, 1])
        [1, 2, 2, 1, 0]
    \"\"\"
    iterable = discretization(iterable)[0]
    index = len(iterable)
    bit = Fenwick(index)
    result = [0] * index
    for item in reversed(iterable):
        index -= 1
        result[index] = bit.query(item)
        bit.update(item, 1)
    return result


def discretization(iterable):
    \"\"\" [1, 2, 4, 2, 5] -> [0, 1, 2, 1, 3] \"\"\"
    iterable = tuple(iterable)
    discrete_dict = dict(zip(sorted(set(iterable)), range(len(iterable))))
    return list(map(discrete_dict.__getitem__, iterable)), {v: k for k, v in discrete_dict.items()}


class Fenwick:
    \"\"\" Simpler FenwickTree \"\"\"

    def __init__(self, x):
        self.bit = [0] * x

    def update(self, idx, x):
        \"\"\"updates bit[idx] += x\"\"\"
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        \"\"\"calc sum(bit[:end])\"\"\"
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        \"\"\"
        Find largest idx such that sum(bit[:idx]) < k
        (!) different from pyrival (just removed the '=')
        \"\"\"
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k > self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1


class PointsCounter:
    def __init__(self, sorted_points):
        \"\"\"
        O(nlogn)
        Example:
            Quadrant([(0, 0), (1, 1), (2, 0), (2, 2), (3, 1), (4, 3)]).bottom_left
            -> [0, 1, 0, 2, 2, 5]
        \"\"\"
        self.data = sorted_points
        self._len = len(self.data)
        self.counter = Counter(self.data)
        self._xx, self._yy = zip(*self.data)
        self._xx = discretization(self._xx)[0]  # No sorting required
        self._yy = discretization(self._yy)[0]
        xy = tuple(zip(self._xx, self._yy))
        x_yy_size = xy[-1][0] + 1
        self._x_yy = [[] for ___ in range(x_yy_size)]  # reversed
        for x, y in xy:
            self._x_yy[x].append(y)
        # inversion
        bit = Fenwick(max(self._yy) + 1)
        self.bottom_left = []
        for nums in self._x_yy:
            for num in nums:
                self.bottom_left.append(bit.query(num))
            for num in nums:
                bit.update(num, 1)
        # other
        y_xx_size = max(self._yy) + 1
        self._y_xx = [[] for ___ in range(y_xx_size)]
        for x, y in xy:
            self._y_xx[y].append(x)

        self.same = [self.counter[self.data[index]] - 1 for index in range(self._len)]

        self.top = [0] * self._len
        self.bottom = [0] * self._len
        self.left = [0] * self._len
        self.right = [0] * self._len
        for index in range(self._len):
            x = self._xx[index]
            y = self._yy[index]
            self.bottom[index] = bisect_left(self._x_yy[x], y)
            self.top[index] = len(self._x_yy[x]) - self.bottom[index] - self.same[index]
            self.left[index] = bisect_left(self._y_xx[y], x)
            self.right[index] = len(self._y_xx[y]) - self.left[index] - self.same[index]

    def __len__(self):
        return self._len


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        points = [(p[0], -p[1]) for p in intervals]
        points.sort()
        pc = PointsCounter(points)
        ans = 0
        same = set()
        for i in range(len(pc)):
            if pc.bottom_left[i] or pc.left[i] or pc.bottom[i]:
                continue
            if pc.same[i]:
                same.add(pc.data[i])
            else:
                ans += 1
        return ans + len(same)
