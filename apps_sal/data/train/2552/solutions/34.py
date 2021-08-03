class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arrLen = len(arr)
        delta = arrLen // 4
        if arrLen == 1:
            return arr[0]

        pre = ''
        i = 0
        while i < arrLen - delta:
            if arr[i] != pre:
                pre = arr[i]
                if arr[i + delta] == pre:
                    return pre
            i += 1
