class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack, res, cur = [], [], ['']
        for i, v in enumerate(expression):
            print(v)
            print(stack)
            print(res, cur)
            if v.isalpha():
                cur = [c + v for c in cur]

            elif v == '{':
                stack.append(res)
                stack.append(cur)
                res, cur = [], ['']
            elif v == '}':
                precur = stack.pop()
                preres = stack.pop()
                cur = [p + c for p in precur for c in res + cur]
                res = preres
            elif v == ',':
                res += cur
                cur = ['']
        return sorted(set(res + cur))
