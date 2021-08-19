class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        result = []
        left = 0
        right = len(arr) - 1
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        while left <= right:
            m_left = abs(m - arr[left])
            m_right = abs(m - arr[right])
            if m_left < m_right:
                result.append(arr[right])
                right -= 1
            elif m_left > m_right:
                result.append(arr[left])
                left += 1
            elif arr[left] > arr[right]:
                result.append(arr[left])
                left += 1
            else:
                result.append(arr[right])
                right -= 1
        return result[0:k]
