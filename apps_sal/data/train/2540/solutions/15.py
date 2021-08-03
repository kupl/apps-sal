class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        A.sort()
        counter = 3
        perimeter = 0
        while counter <= len(A):

            a = A[counter - 3]
            b = A[counter - 2]
            c = A[counter - 1]

            if a + b <= c:
                counter += 1
                continue
            elif b + c <= a:
                counter += 1
                continue
            elif c + a <= b:
                counter += 1
                continue
            perimeter = a + b + c
            if a + b + c > perimeter:
                perimeter = a + b + c

            counter += 1
        return perimeter
