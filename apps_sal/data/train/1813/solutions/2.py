class Solution:

    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        if not books:
            return 0
        h = [0]
        current = 0
        while current < len(books):
            w = books[current][0]
            f = current
            c_h = books[current][1]
            h_i = float('inf')
            while w <= shelf_width and f >= 0:
                h_i = min(c_h + h[f], h_i)
                if f == 0:
                    break
                f -= 1
                w += books[f][0]
                c_h = max(c_h, books[f][1])
            h.append(h_i)
            current += 1
        return h[-1]
