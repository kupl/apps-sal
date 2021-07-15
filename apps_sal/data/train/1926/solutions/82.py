class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        closestOne = self.findClosestProduct(num+1)
        closestTwo = self.findClosestProduct(num+2)
        differenceOne = abs(closestOne[0]-closestOne[1])
        differenceTwo = abs(closestTwo[0]-closestTwo[1])
        if differenceOne > differenceTwo:
            return closestTwo
        else:
            return closestOne
    def findClosestProduct(self,num):
        ##we start from floor of sqrt(num) and go down.
        for i in range(int(math.sqrt(num)),0,-1):
            if num%i == 0:
                return [i,num//i]

