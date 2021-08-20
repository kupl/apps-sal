class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        i = 0
        j = n - 1
        ans = []
        for _ in range(k):
            s1 = abs(arr[i] - median)
            s2 = abs(arr[j] - median)
            if s1 > s2:
                ans.append(arr[i])
                i += 1
            elif s1 == s2:
                if arr[i] > arr[j]:
                    ans.append(arr[i])
                    i += 1
                else:
                    ans.append(arr[j])
                j -= 1
            else:
                ans.append(arr[j])
                j -= 1
        return ans
