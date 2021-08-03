class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        stack, res, cur = [], [], ['']
        for v in expression:

            if v.isalpha():
                cur = [c + v for c in cur]
            elif v == ',':
                res += cur
                cur = ['']
            elif v == '{':
                stack.append(res)
                stack.append(cur)
                res, cur = [], ['']
            elif v == '}':
                preCur = stack.pop()
                preRes = stack.pop()
                cur = [p + c for p in preCur for c in res + cur]
                res = preRes
        return sorted(set(res + cur))
