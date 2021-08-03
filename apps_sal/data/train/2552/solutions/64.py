class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        uniq = list()
        [uniq.append(i) for i in arr if i not in uniq]
        occurs = {i: 0 for i in arr}
        for i in arr:
            occurs[i] += 1
        return [key for key, val in list(occurs.items()) if val / len(arr) > 0.25][0]
