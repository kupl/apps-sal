class Solution:

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for i in range(1, n):
            temp = list()
            for r in result:
                if k == 0:
                    temp.append(r * 10 + r % 10)
                else:
                    back = r % 10
                    if back - k >= 0:
                        temp.append(r * 10 + back - k)
                    if back + k < 10:
                        temp.append(r * 10 + back + k)
            result = temp.copy()
        return result
