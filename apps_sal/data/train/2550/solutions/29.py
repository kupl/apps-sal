class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num=[0,0]
        for i in bills:
            if i ==5:
                num[0]+=1
            elif i==10 and num[0]>=1:
                num[1]+=1
                num[0]-=1
            elif i==20:
                if (num[0]>=1 and num[1]>=1):
                    num[1]-=1
                    num[0]-=1
                elif num[0]>=3:
                    num[0]-=3
                else:
                    return False
            else:
                return False
        return True
