class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr_new = sorted(arr)
        med = arr_new[int((len(arr) - 1) / 2)]

        i = 0
        j = 1
        output = []
        while True:
            if len(output) >= k:
                break
            elif abs(arr_new[-j] - med) >= abs(arr_new[i] - med):
                output.append(arr_new[-j])
                j += 1
            else:
                output.append(arr_new[i])
                i += 1

        return output
