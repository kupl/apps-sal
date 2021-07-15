class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sort = sorted(arr)
        m = sort[int((len(arr) - 1) / 2)]
        # sorted_by_m = {}
        # for n in sort:
        #     curr = abs(n - m)
        #     if curr in sorted_by_m:
        #         sorted_by_m.append(curr)
        #     else:
        #         sorted_by_m = [curr]
        
        sort.reverse()
        sorted_by_m = sorted(sort, key=lambda x: abs(x - m), reverse=True)
        print(m, sorted_by_m)
        return sorted_by_m[:k]
