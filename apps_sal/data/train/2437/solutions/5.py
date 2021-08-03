class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if arr is None:
            return False
        if m <= len(arr) and k * m <= len(arr):
            for s in range(len(arr) - m):
                rec = {}
                for i in range(s, len(arr) - m + 1):
                    if tuple(arr[i:i + m]) not in rec:
                        rec[tuple(arr[i:i + m])] = 1
                    else:
                        if arr[i:i + m] == arr[i - m:i]:
                            rec[tuple(arr[i:i + m])] += 1
                        else:
                            break
                tmp = list(rec.values())
                if k in tmp:
                    return True
        return False
