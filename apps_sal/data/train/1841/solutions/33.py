class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        h = (len(arr) - 1) // 2
        median = arr[h]
        count = 0
        result = []
        i = 0
        j = len(arr) - 1
        while count < k and i <= j:
            strengthI = abs(arr[i] - median)
            strengthJ = abs(arr[j] - median)
            if strengthI == strengthJ:
                if arr[i] > arr[j]:
                    result.append(arr[i])
                    i += 1
                else:
                    result.append(arr[j])
                    j -= 1
            elif strengthI > strengthJ:
                result.append(arr[i])
                i += 1
            else:
                result.append(arr[j])
                j -= 1
            count += 1
        return result
