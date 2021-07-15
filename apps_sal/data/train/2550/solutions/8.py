class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        no_5=0
        no_10=0
        for i in bills:
            if i==5:
                no_5+=1
            elif i==10:
                no_10+=1
                no_5-=1
            else:
                if no_10==0:
                    no_5-=3
                else:
                    no_10-=1
                    no_5-=1
            if no_5<0 or no_10<0:
                return False
        return True
