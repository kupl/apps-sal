def go_bf(i, books, curr_width, ch, shelf_width):
    if i == len(books):
        return 0

    w,h = books[i][0], books[i][1]
    best_h = float(\"inf\")
    if curr_width + w <= shelf_width:
        # if we add higher then we pay, is smaller then it's for free
        diff = max(h - ch, 0)   
        best_h = diff + go_bf(i+1, books, curr_width + w, ch, shelf_width)
    best_h = min(best_h, h + min(best_h, go_bf(i+1, books, w, h, shelf_width)))
    return best_h

def go_memo(i, books, curr_width, ch, shelf_width, memo):
    if i == len(books):
        return 0

    if memo[i][curr_width] == -1:
        w,h = books[i][0], books[i][1]
        best_h = float(\"inf\")
        if curr_width + w <= shelf_width:
            # if we add higher then we pay, is smaller then it's for free
            diff = max(h - ch, 0)   
            best_h = diff + go_memo(i+1, books, curr_width + w, ch + diff, shelf_width, memo)
        best_h = min(best_h, h + min(best_h, go_memo(i+1, books, w, h, shelf_width, memo)))
        memo[i][curr_width] = best_h
    return memo[i][curr_width]

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        memo = [[-1] * (shelf_width + 1) for _ in range(len(books))]
        return go_memo(0, books, 0, 0, shelf_width, memo)
