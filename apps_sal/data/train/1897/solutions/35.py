class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        \"\"\"
        https://leetcode-cn.com/problems/xor-queries-of-a-subarray/solution/zi-shu-zu-yi-huo-cha-xun-by-leetcode-solution/
        * pre[0] = 0
          pre[i] = arr[0] ^ arr[1] ^ ... ^ arr[i - 1]
          arr[Li] ^ ... ^ arr[Ri] = pre[Li] ^ pre[Ri + 1]
        \"\"\"
        # pre = [0]
        # for num in arr:
        #     pre.append(pre[-1] ^ num)
        # ans = list()
        # for x, y in queries:
        #     ans.append(pre[x] ^ pre[y + 1])
        # return ans
    
        # for i in range(len(arr) - 1):
        #     arr[i + 1] ^= arr[i]
        for i in range(1, len(arr)):
            arr[i] = arr[i]^arr[i-1]
        return [arr[j] ^ arr[i - 1] if i else arr[j] for i, j in queries]

