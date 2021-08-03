class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        #print(m, arr)
        l, r = 0, len(arr) - 1
        ret = []
        while k > 0 and l <= r:
            print((l, r))
            al, ar = abs(arr[l] - m), abs(arr[r] - m)
            if al == ar:
                if arr[l] >= arr[r]:
                    ret.append(arr[l])
                    l += 1
                else:
                    ret.append(arr[r])
                    r -= 1
            elif al > ar:
                ret.append(arr[l])
                l += 1
            else:
                ret.append(arr[r])
                r -= 1
            k -= 1
        return ret
