class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) in [0, 1, 2]:
            return False
        max_ele = max(A)
        if A.count(max_ele) > 1:
            return False
        index = A.index(max_ele)
        if index == len(A) - 1 or index == 0:
            return False
        for i in range(0, index):
            print(('values', A[i], A[i + 1]))
            print(('index', i, i + 1))
            if not A[i] < A[i + 1]:
                print('trig1')
                return False
        for i in range(len(A) - 1, index + 1, -1):
            print('hi')
            if not A[i] < A[i - 1]:
                print('trig2')
                return False
        return True
