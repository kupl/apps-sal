class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    test = 0
                    if -a <= arr[i] - arr[j] <= a:
                        test += 1
                    if -b <= arr[j] - arr[k] <= b:
                        test += 1
                    if -c <= arr[i] - arr[k] <= c:
                        test += 1
                    if test == 3:
                        cnt += 1
        return cnt
