class Solution:
    def findLucky(self, arr: List[int]) -> int:
        book = {}.fromkeys(set(arr))
        for key in list(book.keys()):
            book[key] = arr.count(key)
        result = -1
        for key, value in list(book.items()):
            if key == value:
                result = max(result, key)
        return result
