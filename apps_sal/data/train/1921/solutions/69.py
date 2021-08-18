import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stks = []
        self.queue = []
        self.idx2cnt = [0 for _ in range(100000 + 5)]

    def _leftmost_idx(self):
        ret = len(self.stks)
        while len(self.queue) > 0:
            idx = self.queue[0]
            if self.idx2cnt[idx] < self.capacity:
                ret = idx
                break
            else:
                heapq.heappop(self.queue)
        return ret

    def _rightmost_idx(self):
        idx = len(self.stks) - 1
        while idx >= 0 and self.idx2cnt[idx] == 0:
            idx -= 1
        return idx

    def _pop(self, idx):
        if self.idx2cnt[idx] == 0:
            return -1
        ret = self.stks[idx].pop()
        if self.idx2cnt[idx] == self.capacity:
            heapq.heappush(self.queue, idx)
        self.idx2cnt[idx] -= 1
        while idx > 0 and self.idx2cnt[idx] == 0 and idx == len(self.stks) - 1:
            self.stks.pop()
            idx -= 1
        return ret

    def push(self, val: int) -> None:
        idx = self._leftmost_idx()
        if idx == len(self.stks):
            self.stks.append([])
            heapq.heappush(self.queue, idx)
        self.stks[idx].append(val)
        self.idx2cnt[idx] += 1

    def pop(self) -> int:
        idx = self._rightmost_idx()
        return self._pop(idx)

    def popAtStack(self, index: int) -> int:
        return self._pop(index)
