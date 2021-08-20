class Solution:

    def binaryGap(self, N: int) -> int:
        bit_list = bin(N)[2:]
        stack = []
        dis = 0
        for b in bit_list:
            if not stack and b == '1':
                stack.append(b)
            elif stack and b == '0':
                stack.append(b)
            elif stack and b == '1':
                dis = max(dis, len(stack))
                stack = ['1']
        return dis
