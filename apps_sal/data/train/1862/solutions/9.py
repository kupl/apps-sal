class Solution:

    def pancakeSort(self, arr: List[int]) -> List[int]:
        results = []
        end = len(arr)
        while end > 1:
            max_idx = arr.index(max(arr[:end]))
            if max_idx == end - 1:
                end -= 1
            else:
                if max_idx > 0:
                    results.append(max_idx + 1)
                    arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
                results.append(end)
                arr[:end] = reversed(arr[:end])
                end -= 1
        print(arr)
        return results
