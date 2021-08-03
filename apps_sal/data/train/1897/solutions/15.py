class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        x = 0
        xors = []
        for i in arr:
            x ^= i
            xors.append(x)
        return [xors[i[1]] ^ xors[i[0]] ^ arr[i[0]] for i in queries]
