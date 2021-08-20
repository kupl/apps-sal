import heapq


def coor_neighbor(coor, dxs, dys):
    (x, y) = coor
    for dx in dxs:
        for dy in dys:
            yield (x + dx, y + dy)


def coor_bottoms(coor):
    return coor_neighbor(coor, (-1, 0, 1), (-1,))


def coor_tops(coor):
    return coor_neighbor(coor, (-1, 0, 1), (1,))


def coor_sibs(coor):
    return coor_neighbor(coor, (-2, -1, 1, 2), (0,))


class Figure:

    def __init__(self, coors):
        self._coors = dict()
        self._stables_min = []
        self._stables_max = []
        self._pushed = set()
        self._dropped = set()
        cubes = dict()
        self._bots = dict()
        self._tops = dict()
        for (idx, coor) in enumerate(coors):
            cubes[coor] = idx
            self._coors[idx] = coor
            self._bots[idx] = set()
            self._tops[idx] = set()
        coor_set = set(coors)
        for (idx, coor) in enumerate(coors):
            for bottom in coor_bottoms(coor):
                if bottom in coor_set:
                    self._bots[idx].add(cubes[bottom])
            for top in coor_tops(coor):
                if top in coor_set:
                    self._tops[idx].add(cubes[top])
        for idx in self._coors:
            if self.isdroppable(idx):
                self.push(idx)

    def sibs(self, idx):
        for top_idx in self._tops[idx]:
            for sib_idx in self._bots[top_idx]:
                if sib_idx not in self._dropped:
                    yield sib_idx

    def bottom_count(self, idx):
        return len(self._bots[idx])

    def isdroppable(self, idx):
        return all((len(self._bots[top_idx]) > 1 for top_idx in self._tops[idx]))

    def push(self, idx):
        if idx not in self._pushed:
            heapq.heappush(self._stables_min, idx)
            heapq.heappush(self._stables_max, -idx)
            self._pushed.add(idx)

    def unpush(self, idx):
        if idx in self._pushed:
            self._pushed.remove(idx)

    def drop(self, idx):
        if idx not in self._pushed:
            return False
        self._pushed.remove(idx)
        self._dropped.add(idx)
        for bot_idx in self._bots[idx]:
            self._tops[bot_idx].remove(idx)
        for top_idx in self._tops[idx]:
            self._bots[top_idx].remove(idx)
        coor = self._coors[idx]
        for bot_idx in self._bots[idx]:
            if self.isdroppable(bot_idx):
                self.push(bot_idx)
        for sib_idx in self.sibs(idx):
            if not self.isdroppable(sib_idx):
                self.unpush(sib_idx)
        return True

    def drop_min(self):
        while True:
            if not self._stables_min:
                return None
            min_idx = heapq.heappop(self._stables_min)
            if self.drop(min_idx):
                return min_idx

    def drop_max(self):
        while True:
            if not self._stables_max:
                return None
            max_idx = -heapq.heappop(self._stables_max)
            if self.drop(max_idx):
                return max_idx

    def __bool__(self):
        return len(self._coors) != len(self._dropped)


def input_tuple():
    return tuple(map(int, input().split()))


def result_add(result, base, num):
    return (result * base + num) % (10 ** 9 + 9)


N = int(input())
coors = [input_tuple() for _ in range(N)]
figure = Figure(coors)
result = 0
while True:
    if not figure:
        break
    result = result_add(result, N, figure.drop_max())
    if not figure:
        break
    result = result_add(result, N, figure.drop_min())
print(result)
