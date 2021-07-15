class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        stack = []
        def solve(index):
            if stack and int(stack[-1]) > 2**31-1:
                return False
            #print(stack, S[index:])
            if index == len(S):
                return len(stack) >= 3
            if len(stack) < 2:
                if S[index] == '0':
                    stack.append('0')
                    if solve(index+1):
                        return True
                    stack.pop()
                    return False
                for i in range(index, len(S)):
                    stack.append(S[index:i+1])
                    if solve(i+1):
                        return True
                    stack.pop()
            elif int(stack[-1]) + int(stack[-2]) > int(S[index:]):
                return False
            else:
                if S[index] == '0':
                    if stack[-1] == '0' and stack[-2] == '0':
                        stack.append('0')
                        if solve(index+1):
                            return True
                        stack.pop()
                    return False
                for i in range(index, len(S)):
                    if int(stack[-1]) + int(stack[-2]) == int(S[index:i+1]):
                        stack.append(S[index:i+1])
                        if solve(i+1):
                            return True
                        stack.pop()
            return False
        solve(0)
        return stack
