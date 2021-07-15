class Solution:
    def thousandSeparator(self, n: int) -> str:
        arr = []
        i, count = 0, 0
        num = str(n)
        while i < len(num):
            if count != 3:
                arr.append(num[~i])
                i += 1
                count += 1
            else:
                arr.append('.')
                count = 0
                
        return ''.join(arr[::-1])

