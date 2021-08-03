class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        stack = []
        for i in range(len(A) - 1, -1, -1):
            if stack != [] and stack[-1] < A[i]:
                break
            stack.append(A[i])

        if len(stack) == len(A):
            return A

        # print(i)
        stack = stack[::-1]
        low, high = 0, len(stack) - 1
        while low < high - 1:
            mid = (low + high) // 2
            if stack[mid] >= A[i]:
                high = mid - 1
            else:
                low = mid
        # print(stack[high])
        if stack[high] >= A[i]:
            high -= 1

        l = high - 1
        while l >= 0 and stack[l] == stack[high]:
            l -= 1
        l += 1
        # print(l)
        temp = A[i]
        A[i] = A[i + l + 1]
        A[i + l + 1] = temp

        return A
