class Solution:

    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        self.shelf = defaultdict(list)

        @lru_cache(None)
        def helper(i):
            if i == len(books):
                return 0
            width = 0
            height = 0
            out = float('inf')
            while width < shelf_width and i < len(books):
                (w, h) = books[i]
                width += w
                if width > shelf_width:
                    break
                height = max(height, h)
                others = helper(i + 1)
                out = min(height + others, out)
                i += 1
            return out
        out = helper(0)
        return out
