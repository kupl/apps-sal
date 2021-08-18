class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = arr[(n - 1) // 2]
        strong = []
        i, j = 0, len(arr) - 1
        while i <= j:
            if abs(arr[i] - m) <= abs(arr[j] - m):
                strong.append(arr[j])
                j -= 1
            else:
                strong.append(arr[i])
                i += 1
        return(strong[:k])
