class Solution:
    def toHex(self, num):
        def toHexUnsigned(num):
            num_hex = []
            while num // 16 > 0:
                digit = num % 16
                if digit >= 10:
                    num_hex.append(chr(digit - 10 + ord('a')))
                else:
                    num_hex.append(str(digit))
                num = num // 16

            if num >= 10:
                num_hex.append(chr(num - 10 + ord('a')))
            elif num > 0:
                num_hex.append(str(num))

            return "".join(num_hex[::-1])

        if num == 0:
            return "0"
        if num < 0:
            return toHexUnsigned(2**32 + num)
        else:
            return toHexUnsigned(num)
