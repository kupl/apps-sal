from collections import Counter
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        n = len(A)
        groups = 0
        taken = [0]*n
        even_counters = list(map(Counter, [z[::2] for z in A]))
        odd_counters = list(map(Counter, [z[1::2] for z in A]))
        for i in range(n):
            if taken[i]==0:
                oci = odd_counters[i]
                eci = even_counters[i]
                for j in range(i+1, n):
                    if taken[j]==1:
                        continue
                    ocj = odd_counters[j]
                    ecj = even_counters[j]
                    if oci==ocj and eci==ecj:
                        taken[j] = 1
                groups += 1
        return groups

