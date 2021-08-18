class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        m = (len(arr) - 1) // 2
        mv = arr[m]
        ans = []
        i, j = 0, len(arr) - 1
        while(k and i <= j):
            rv, lv = abs(arr[j] - mv), abs(arr[i] - mv)
            if rv > lv:
                ans.append(arr[j])
                j -= 1
                k -= 1
            elif lv > rv:
                ans.append(arr[i])
                i += 1
                k -= 1
            else:
                if arr[j] > arr[i]:
                    ans.append(arr[j])
                    j -= 1
                    k -= 1
                else:
                    ans.append(arr[i])
                    i += 1
                    k -= 1
        return ans
