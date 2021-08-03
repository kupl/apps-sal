class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        for i in range(n, 0, -1):
            for j in range(i - 1):
                if arr[j] == i:
                    ans.append(j + 1)
                    ans.append(i)
                    print((j, i))
                    arr = list(reversed(arr[:j + 1])) + arr[j + 1:]
                    print(arr)
                    arr = list(reversed(arr[:i])) + arr[i:]
                    print(arr)
                    break
        return ans
