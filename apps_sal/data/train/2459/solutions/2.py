class Solution:

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        '\n         s = []\n         hexChar= [\'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \'a\', \'b\', \'c\', \'d\', \'e\', \'f\']\n         if num == 0:\n             return \'0\'\n         while num:\n             s.append(hexChar[num % 16])\n             num = num // 16\n         return "".join(s[::-1])\n         hex(int())\n         hex(num & 0b)\n         '
        return '%x' % (num & 4294967295)
