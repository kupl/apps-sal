class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        list = []
        i = 0
        j = len(arr) - 1
        while i <= j and k > 0:
            if abs(arr[i] - median) > abs(arr[j] - median):
                list.append(arr[i])
                i += 1
            else:
                list.append(arr[j])
                j -= 1
            k -= 1
        return list
