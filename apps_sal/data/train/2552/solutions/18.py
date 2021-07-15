class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        else:
            appear = -(-len(arr) // 4)
            dict ={}
            for i in arr:
                if i not in dict:
                    dict[i] = 1
                else:
                    dict[i] += 1
                if dict[i] > appear:
                    return i
