class Solution:

    def removeDuplicates(self, S: str) -> str:

        def delete(S, index):
            S = S[:index] + S[index + 1:]
            return S
        stack = []
        stack_top = -1
        pointer = 0
        while pointer < len(S):
            if len(stack) == 0 or S[pointer] != stack[stack_top]:
                stack.append(S[pointer])
                pointer += 1
                stack_top += 1
            else:
                S = delete(S, pointer - 1)
                pointer -= 1
                S = delete(S, pointer)
                stack.pop(-1)
                stack_top -= 1
        return S
