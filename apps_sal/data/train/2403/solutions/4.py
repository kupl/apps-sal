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
        while i <= int(num ** 0.5):
            if num % i == 0:
                sum += i
                if i != num // i:
                    sum += num // i
            i += 1
        return num == sum
        '\n    #    my first solution...beat 28%...\n         \n         if num <= 5:\n             return False\n         \n         factor = [1]\n         i = 2\n         while i <= int(math.sqrt(num)):\n             if num%i == 0:\n                 factor.append(i)\n                 if i != num//i:\n                     factor.append(num//i)\n             i += 1\n         return num == sum(factor)\n         '
