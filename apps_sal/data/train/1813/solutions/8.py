class Solution:
    def minHeightShelves(self, books: List[List[int]], sw: int) -> int:
        n = len(books)
        mem = [None] * (n + 1)
        mem[-1] = 0

        def f(pos):
            if mem[pos] is not None:
                return mem[pos]

            w, h = 0, 0
            value = float('inf')

            for i in range(pos, n):
                w += books[i][0]
                h = max(h, books[i][1])
                if w > sw:
                    break
                value = min(value, f(i + 1) + h)

            mem[pos] = value
            return mem[pos]

        return f(0)
