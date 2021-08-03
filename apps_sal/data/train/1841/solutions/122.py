class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sorted_arr = sorted(arr)
        n = len(arr)
        median = sorted_arr[(n - 1) // 2]

        results = []
        start_idx, end_idx = 0, n - 1

        while k > 0 and start_idx <= end_idx:
            if abs(sorted_arr[start_idx] - median) < abs(sorted_arr[end_idx] - median):
                results.append(sorted_arr[end_idx])
                end_idx -= 1
            elif abs(sorted_arr[start_idx] - median) > abs(sorted_arr[end_idx] - median):
                results.append(sorted_arr[start_idx])
                start_idx += 1
            else:
                if sorted_arr[start_idx] > sorted_arr[end_idx]:
                    results.append(sorted_arr[start_idx])
                    start_idx += 1
                else:
                    results.append(sorted_arr[end_idx])
                    end_idx -= 1
            k -= 1

        return results
