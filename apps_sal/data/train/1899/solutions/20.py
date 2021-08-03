import queue


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:

        def adjacent(i, q):
            nonlocal A

            l = []

            if i > 0:
                l.append([i - 1, q])
            if i < len(A) - 1:
                l.append([i + 1, q])
            if q > 0:
                l.append([i, q - 1])
            if q < len(A[0]) - 1:
                l.append([i, q + 1])

            return l

        def fill(i, q):
            nonlocal A

            A[i][q] = 2

            qu = queue.Queue()
            qu.put([i, q])
            seen = set()

            while not qu.empty():

                current = qu.get()
                seen.add(tuple(current))

                l = adjacent(current[0], current[1])

                for a, b in l:
                    if A[a][b] == 1:
                        A[a][b] = 2
                        qu.put([a, b])

            return seen

        starts = []
        broken = False
        for i in range(len(A)):
            for q in range(len(A[0])):

                if A[i][q] == 1:

                    starts = fill(i, q)
                    broken = True
                    break
            if broken:
                break

        qu = queue.Queue()

        for el in list(starts):
            qu.put(list(el) + [0])

        while not qu.empty():
            current = qu.get()

            l = adjacent(current[0], current[1])

            for i, q in l:
                if A[i][q] == 1:
                    return current[2]
                elif A[i][q] == 0:
                    A[i][q] = 2
                    qu.put([i, q, current[2] + 1])
