class Solution:

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        save = []
        num = (num + 4294967296) % 4294967296
        while num > 0:
            save.append(check[num % 16])
            num //= 16
        return ''.join(save)[::-1]
