class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 5:
            return False

        sum = 1
        i = 2
        while i <= int(num**0.5):
            if num % i == 0:
                sum += i
                if i != num // i:
                    sum += num // i
            i += 1
        return num == sum

        """
         
         if num <= 5:
             return False
         
         factor = [1]
         i = 2
         while i <= int(math.sqrt(num)):
             if num%i == 0:
                 factor.append(i)
                 if i != num//i:
                     factor.append(num//i)
             i += 1
         return num == sum(factor)
         """
