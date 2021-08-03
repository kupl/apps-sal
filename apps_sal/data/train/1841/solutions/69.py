class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        p = (len(arr) - 1) // 2
        med = arr[p]

        print(med)
        a1 = arr[:p]
        a2 = arr[p:]

        ans = []
        while k > 0:
            if len(a2) > 0 and len(a1) > 0:
                diff = abs(a2[-1] - med) - abs(a1[0] - med)
                if diff >= 0:
                    ans.append(a2.pop(-1))
                else:
                    ans.append(a1.pop(0))
            elif len(a2) > 0:
                ans.append(a2.pop(-1))
            elif len(a1) > 0:
                ans.append(a1.pop(0))
            k -= 1
        return ans
