class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr = sorted(arr)
        med_idx = (n - 1) // 2
        med_val = arr[med_idx]

        dist = []
        for i in range(len(arr)):
            dist.append((abs(arr[i] - med_val), arr[i], i))

        dist.sort(key=lambda x: (x[0], x[1]), reverse=True)

        ans = []
        for i in range(len(dist)):
            if i == k:
                break
            ans.append(arr[dist[i][2]])
        return ans
