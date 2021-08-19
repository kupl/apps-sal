class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # use extra array to store the information
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] ^ arr[i]
        ans = []
        for query in queries:
            start = query[0]
            end = query[1]
            if start == 0:
                ans.append(prefix[end])
            else:
                ans.append(prefix[start - 1] ^ prefix[end])

        return ans
