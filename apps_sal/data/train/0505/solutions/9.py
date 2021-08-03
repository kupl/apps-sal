class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # leftIndex, rightIndex = [],[]
        # for index, item in enumerate(s):
        #     if item == '(': leftIndex.append(index)
        #     if item == ')': rightIndex.append(index)
        # print(leftIndex,rightIndex)
        stack = []
        p = []
        for index, item in enumerate(s):
            if item == '(':
                stack.append(index)
            elif item == ')' and stack:
                p.append([stack.pop(), index])
        # s = [i for i in s.replace(')','_').replace('(','_')]
        # for [l,r] in p:
        #     s[l] = '('
        #     s[r] = ')'
        # return ''.join(s).replace('_','')

        s = s.replace(')', '_').replace('(', '_')
        for [l, r] in p:
            s = s[:l] + '(' + s[l + 1:r] + ')' + s[r + 1:]
        return s.replace('_', '')
