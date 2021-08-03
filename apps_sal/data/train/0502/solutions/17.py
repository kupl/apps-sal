class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

        heap = []
        sizes = {}
        component = 0

        for i in initial:
            # print(\"graph\", graph, heap)
            if graph[i][i] < 0:
                heappush(heap, (-sizes[component], i, graph[i][i]))
                continue

            queue = deque([i])
            # print(\"outer queue\", queue)
            size = 0
            component = component - 1

            while len(queue) > 0:

                current = queue.popleft()
                # print(current)

                if graph[current][current] == 1:
                    size = size + 1
                    graph[current][current] = component
                    queue.extend(i for (i, x) in enumerate(graph[current]) if x == 1)
                    # print(\"queue\", current, queue)

            heappush(heap, (-size, i, component))
            sizes[component] = size

        # print(\"final heap\", heap)

        return self.select(heap)

    def select(self, heap):

        if len(heap) == 1:
            return heap[0][1]

        res = heappop(heap)
        others = []
        while len(heap) > 0 and res[0] == heap[0][0] and res[2] == heap[0][2]:
            others.append(heappop(heap))

        if len(others) == 1 and len(heap) == 0 or len(others) == 0:
            return res[1]

        if len(heap) == 0:
            return res[1]

        return self.select(heap)
