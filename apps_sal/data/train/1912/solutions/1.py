class Solution:

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        st = 0
        ed = len(letters) - 1
        if target < letters[0] or target > letters[-1]:
            return letters[0]
        while st <= ed:
            mid = st + (ed - st) // 2
            if letters[mid - 1] < target and letters[mid] > target:
                return letters[mid]
            if letters[mid] == target:
                ans = letters[0]
                i = mid
                while i < len(letters):
                    if letters[i] != target:
                        return letters[i]
                    i += 1
                return ans
            if letters[mid] < target:
                st = mid + 1
            else:
                ed = mid - 1
