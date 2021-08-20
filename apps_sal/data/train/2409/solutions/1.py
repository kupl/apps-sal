class Solution:

    def maximum69Number(self, num: int) -> int:
        res = 0
        li = list(str(num))
        first = -1
        for i in range(len(li)):
            if li[i] == '6':
                first = i
                break
        li[first] = '9'
        return int(''.join(li))
