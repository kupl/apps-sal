class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        res = [val for val in A]
        length = len(A)
        start = 0
        haveInvertedPos = False
        # 寻找最后一个逆序位置
        for i in range(length - 1):
            if A[i] <= A[i + 1]:
                pass
            else:
                start = i
                haveInvertedPos = True
        # 没有逆序位置
        if not haveInvertedPos:
            return res
        target = start + 1
        temp = A[target]
        for i in range(start + 1, length):
            if A[i] < A[start] and A[i] > temp:
                temp = A[i]
                target = i
        # print(start, target)
        res[start], res[target] = res[target], res[start]
        return res
