class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5: 0, 10: 0, 20: 0}
        for i in bills:
            if i == 5:
                dic[5] += 1
            if i == 10:
                if dic[5] < 1:
                    return False
                dic[10] += 1
                dic[5] -= 1
            if i == 20:
                dic[20] += 1
                if dic[10] >= 1 and dic[5] >= 1:
                    dic[5] -= 1
                    dic[10] -= 1
                elif dic[10] < 1 and dic[5] >= 3:
                    dic[5] -= 3
                else:
                    return False
            print((i, dic))
        return True
