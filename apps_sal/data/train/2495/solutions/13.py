def sort(list_a):
    low = []
    high = []
    if len(list_a) <= 1:
        return list_a
    else:
        v = list_a.pop()
        for i in range(len(list_a)):
            if list_a[i] > v:
                high.append(list_a[i])
            else:
                low.append(list_a[i])
        return sort(low) + [v] + sort(high)


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target = sort(target)
        arr = sort(arr)
        if arr == target:
            return True
        else:
            return False
