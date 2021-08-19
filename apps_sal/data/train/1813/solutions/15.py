class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:

        # chanllenge is when to switch to new level

        def naive(books, shelf_width, remain=None):
            if remain is None:
                remain = shelf_width
            shelf = []
            shelves = [shelf]
            for w, h in books:
                cur_w = sum(x for x, y in shelf)
                cur_h = max((y for x, y in shelf), default=0)
                added = False
                # print((w,h), cur_w, cur_h)
                if cur_w + w <= shelf_width:
                    if cur_h > 0 and h - cur_h >= 2:  # do some lookahead
                        pass
                    else:
                        shelf.append((w, h))
                        added = True
                if not added:
                    shelf = [(w, h)]
                    shelves.append(shelf)
                # print('levels:', len(shelves), sum(max((y for x,y in s), default=0) for s in shelves), shelves)
            return sum(max(y for x, y in s) for s in shelves)

        return naive(books, shelf_width)

    def minHeightShelves1(self, books: List[List[int]], shelf_width: int) -> int:
        # put the highest books first
        pass

    # https://leetcode.com/problems/filling-bookcase-shelves/discuss/323350/Python-Clean-DP-Solution-2D-Knapsack
    # It's a kind of 2D knapsack problem.
    # The core recurrence function is dp[i+1] = min(dp[k] + h for k in {j+1,...,i}).

    # j is the furthest index that {books[j+1],...,books[i]} can be placed in one row.
    # It depends on the widths of those books. books[j] can't be placed into the same row with books[i]
    # otherwise the width would exceed the shelf_width.
    # k is each candidate index that {{books[k],...,books[i]}} are proposed to be placed in the same row.
    # h is the maximum height among {books[k],...,books[i]}.

    def minHeightShelves(self, books, shelf_width):
        def height(i, j):
            return max(books[x][1] for x in range(i, j))

        dp = [0]
        for i in range(len(books)):
            w, j = books[i][0], i
            while j >= 0 and w <= shelf_width:     # find out j, so w should be ahead of j
                j -= 1
                w += books[j][0]
            dp.append(min(dp[k] + height(k, i + 1) for k in range(j + 1, i + 1)))
        return dp[-1]
