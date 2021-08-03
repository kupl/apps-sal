class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def generateGray(n):
            if (n <= 0):
                return

            arr = list()

            arr.append(\"0\")
            arr.append(\"1\")

            i = 2
            j = 0
            while(True):

                if i >= 1 << n:
                    break

                for j in range(i - 1, -1, -1):
                    arr.append(arr[j])

                for j in range(i):
                    arr[j] = \"0\" + arr[j]

                for j in range(i, 2 * i):
                    arr[j] = \"1\" + arr[j]
                i = i << 1

            return arr
        
        def rotateArr(arr, i):
            return arr[-i:] + arr[:-i]
        
        arr = generateGray(n)
        start = \"{0:b}\".format(start)
        res = ''
        if len(start) != n:
            d = n - len(start)
            for i in range(d):
                res += '0'
            start = res + start
        arr = rotateArr(arr, len(arr) - arr.index(start))
        return list(map(lambda x: int(x, 2), arr))
