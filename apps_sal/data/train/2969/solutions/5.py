from collections import deque

INF = 1000000


class Field:
    def __init__(self, n, agents):
        self.n = n
        self.agents = agents
        self.table = [[INF] * n for _ in range(n)]
        self._queue = deque()
        self._calculate_safety()

    def _calculate_safety(self):
        for i, j in self.agents:
            if 0 <= i < self.n and 0 <= j < self.n:
                self._add_to_queue(i, j, 0)
        self._process_queue()

    def _add_to_queue(self, i, j, value):
        self._queue.append((i, j, value))

    def _process_queue(self):
        while self._queue:
            i, j, value = self._queue.popleft()
            if self.table[i][j] != INF:
                continue
            self.table[i][j] = value

            if i < self.n - 1:
                self._add_to_queue(i + 1, j, value + 1)

            if i > 0:
                self._add_to_queue(i - 1, j, value + 1)

            if j < self.n - 1:
                self._add_to_queue(i, j + 1, value + 1)

            if j > 0:
                self._add_to_queue(i, j - 1, value + 1)

    @property
    def safest_places(self):
        locations = []
        max_el = 1
        for i in range(self.n):
            for j in range(self.n):
                if self.table[i][j] > max_el:
                    max_el = self.table[i][j]
                    locations = [(i, j)]
                elif self.table[i][j] == max_el:
                    locations.append((i, j))
        return locations


def advice(agents, n):
    field = Field(n, agents)
    return field.safest_places
