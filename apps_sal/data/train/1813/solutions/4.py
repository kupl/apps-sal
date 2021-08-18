class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        subsoln = [0 for _ in range(len(books) + 1)]

        for prev_idx, (w, h) in enumerate(books):
            cur_idx = prev_idx + 1
            subsoln[cur_idx] = subsoln[prev_idx] + h

            cur_w = w
            cur_h = h
            while prev_idx >= 1 and cur_w + books[prev_idx - 1][0] <= shelf_width:
                cur_h = max(cur_h, books[prev_idx - 1][1])
                cur_w += books[prev_idx - 1][0]
                subsoln[cur_idx] = min(subsoln[cur_idx], subsoln[prev_idx - 1] + cur_h)
                prev_idx -= 1
        print(subsoln)

        return subsoln[-1]
