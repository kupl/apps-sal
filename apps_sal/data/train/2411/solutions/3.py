class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m3 = [nums[0]]
        for y in nums[1:]:
            if m3[0] != y:
                if len(m3) == 1:
                    if m3[0] > y:
                        m3.append(y)
                    else:
                        m3.insert(0, y)
                elif m3[1] != y:
                    if m3[0] < y:
                        m3.insert(0, y)
                    elif m3[1] < y:
                        m3.insert(1, y)
                    else:
                        m3.append(y)
                    break

        if len(m3) < 3:
            return max(m3)

        for y in nums[3:]:
            if y == m3[0] or y == m3[1] or y <= m3[2]:
                continue
            m3.pop()
            if y > m3[0]:
                m3.insert(0, y)
            elif y > m3[1]:
                m3.insert(1, y)
            else:
                m3.append(y)
        return m3[2]
