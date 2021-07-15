class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        from collections import deque
        fives = deque()
        tens = deque()
        try:
            for i in bills:
                if i==5:
                    fives.append(5)
                elif i==10:
                    tens.append(10)
                    fives.pop()
                else:
                    if len(tens) !=0 and len(fives)!=0:
                        tens.pop()
                        fives.pop()
                    else:
                        fives.pop()
                        fives.pop()
                        fives.pop()
        except IndexError:
            return False
        return True


