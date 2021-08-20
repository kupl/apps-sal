class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ret = 0
        subArrs = []
        starting = 0
        ending = len(arr)
        for i in range(len(arr)):
            while ending >= starting:
                if (ending - starting) % 2 != 0:
                    subArrs += [arr[starting:ending]]
                    ending -= 2
                else:
                    ending -= 1
            starting += 1
            ending = len(arr)
        for i in subArrs:
            for j in i:
                ret += j
        return ret
