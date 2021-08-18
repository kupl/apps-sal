class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:

        def naive(books, shelf_width, remain=None):
            if remain is None:
                remain = shelf_width
            shelf = []
            shelves = [shelf]
            for w, h in books:
                cur_w = sum(x for x, y in shelf)
                cur_h = max((y for x, y in shelf), default=0)
                added = False
                if cur_w + w <= shelf_width:
                    if cur_h > 0 and h - cur_h >= 2:
                        pass
                    else:
                        shelf.append((w, h))
                        added = True
                if not added:
                    shelf = [(w, h)]
                    shelves.append(shelf)
            return sum(max(y for x, y in s) for s in shelves)

        return naive(books, shelf_width)

    def minHeightShelves1(self, books: List[List[int]], shelf_width: int) -> int:
        pass

    def minHeightShelves(self, books, shelf_width):
        def height(i, j):
            return max(books[x][1] for x in range(i, j))

        dp = [0]
        for i in range(len(books)):
            w, j = books[i][0], i
            while j >= 0 and w <= shelf_width:
                j -= 1
                w += books[j][0]
            dp.append(min(dp[k] + height(k, i + 1) for k in range(j + 1, i + 1)))
        return dp[-1]
