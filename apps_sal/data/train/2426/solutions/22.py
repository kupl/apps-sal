class Solution:

    def smallestRangeI(self, A: List[int], K: int) -> int:
        ks = [K for a in A]
        ks_left = True
        last_change = 0
        while ks_left and max(A) - min(A) > 0 and (max(A) - min(A) != last_change):
            last_change = max(A) - min(A)
            ks_left = False
            average = sum(A) / len(A)
            for i in range(len(A)):
                difference = A[i] - average
                if -ks[i] <= difference <= ks[i]:
                    A[i] = average
                    ks[i] = abs(ks[i] - abs(difference))
                elif -ks[i] > difference:
                    A[i] += ks[i]
                    ks[i] = 0
                else:
                    A[i] -= ks[i]
                    ks[i] = 0
                if ks[i] > 0:
                    ks_left = True
        print((ks, A))
        return int(max(A) - min(A))
