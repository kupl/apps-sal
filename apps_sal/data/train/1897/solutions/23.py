class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [arr[0]]
        for i in range(1, len(arr)):
            prefix.append(prefix[-1] ^ arr[i])
        result = []
        for s, e in queries:
            if s == 0:
                result.append(prefix[e])
            else:
                result.append(prefix[e] ^ prefix[s - 1])
        return result
