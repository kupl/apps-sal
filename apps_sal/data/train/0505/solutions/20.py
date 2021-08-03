class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pt = {'(': [], ')': []}

        for i in range(len(s)):
            if s[i].isalpha() and s[i].islower():
                continue
            elif s[i] == '(':
                pt['('].append(i)
            elif s[i] == ')':
                pt[')'].append(i)

        to_remove = []

        while pt['('] and pt[')']:
            if pt['('][0] < pt[')'][0]:
                del pt['('][0]
                del pt[')'][0]
            else:
                to_remove.append(pt[')'][0])
                del pt[')'][0]

        if pt['(']:
            to_remove.extend(pt['('])
        if pt[')']:
            to_remove.extend(pt[')'])

        res = ''
        prev = 0
        for i in to_remove:
            res += s[prev:i]
            prev = i + 1
        res += s[prev:]

        return res
