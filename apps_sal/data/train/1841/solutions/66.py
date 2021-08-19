class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        n = len(arr)
        if k == n:
            return arr
        if n % 2 == 0:
            median = arr[n // 2 - 1]
        else:
            median = arr[n // 2]
        i = 0
        j = n - 1
        answer = []
        while True:
            if arr[j] - median >= median - arr[i]:
                answer.append(arr[j])
                j -= 1
            else:
                answer.append(arr[i])
                i += 1
            if len(answer) == k:
                return answer
