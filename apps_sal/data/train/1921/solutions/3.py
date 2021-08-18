import collections
import heapq

StackAndFlags = collections.namedtuple('StackAndFlags', [
    'stack', 'on_push_heap', 'on_pop_heap'])


class DinnerPlates:

    def __init__(self, capacity: int):
        self._cap = capacity
        self._stacks = []
        self._next_push_heap = []
        self._next_pop_heap = []

    def _push_to_top(self, val):
        i = self._next_push_heap[0]
        assert self._stacks[i].on_push_heap
        self._stacks[i].stack.append(val)
        if len(self._stacks[i].stack) == self._cap:
            self._stacks[i] = self._stacks[i]._replace(on_push_heap=False)
            heapq.heappop(self._next_push_heap)
        if not self._stacks[i].on_pop_heap:
            self._stacks[i] = self._stacks[i]._replace(on_pop_heap=True)
            heapq.heappush(self._next_pop_heap, -i)

    def push(self, val: int) -> None:
        if not self._next_push_heap:
            self._stacks.append(StackAndFlags([], True, True))
            new_i = len(self._stacks) - 1
            heapq.heappush(self._next_push_heap, new_i)
            heapq.heappush(self._next_pop_heap, -new_i)
        self._push_to_top(val)

    def pop(self) -> int:
        i = -1
        while self._next_pop_heap:
            j = -self._next_pop_heap[0]
            if self._stacks[j].stack:
                i = j
                break
            else:
                heapq.heappop(self._next_pop_heap)
                self._stacks[j] = self._stacks[j]._replace(on_pop_heap=False)
        if i < 0:
            return -1
        return self.popAtStack(i)

    def popAtStack(self, index: int) -> int:
        if index >= len(self._stacks) or not self._stacks[index].stack:
            return -1
        ret = self._stacks[index].stack.pop()
        if not self._stacks[index].on_push_heap:
            self._stacks[index] = self._stacks[index]._replace(on_push_heap=True)
            heapq.heappush(self._next_push_heap, index)
        return ret
