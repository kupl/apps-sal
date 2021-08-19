class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        N = len(arr)
        median = arr[(N - 1) // 2]
        # easy to see that in the sorted array, if x is before y and smaller than the
        # median, x is stronger than y, and likewise if y is after x and both are after the median, y is stronger than x.
        # so only need to check either end, since we know arr[0] and arr[N-1] are
        # the only candidates for 'strength'

        lp = 0
        rp = N - 1

        output = []
        for i in range(k):
            lps = abs(arr[lp] - median)
            rps = abs(arr[rp] - median)
            if rps >= lps:
                output.append(arr[rp])
                rp -= 1
                continue
            else:  # rps >= lps. if equal we choose the right value
                output.append(arr[lp])
                lp += 1
        return output
