class Solution:

    def getStrongest2(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        dp = [[float('inf') for i in range(len(arr))] for i in range(len(arr))]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if abs(arr[i] - m) > abs(arr[j] - m):
                    strong = arr[i]
                elif abs(arr[i] - m) == abs(arr[j] - m):
                    strong = arr[i] if arr[i] > arr[j] else arr[j]
                else:
                    strong = arr[j]
                dp[i][j] = strong
        for line in dp:
            print(line)
        print()

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        med = sorted(arr)[(len(arr) - 1) // 2]
        return sorted(arr, key=lambda x: (abs(x - med), x))[-k:]
