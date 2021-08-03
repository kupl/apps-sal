class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # print(expression, len(expression))
        def helper(words1, words2):
            # print(words1, words2)
            s = set([])
            for word in words1:
                s.update([word + w for w in words2])
            return list(s)
        
        if len(expression) == 1:
            return [expression]
        n = len(expression)
        b = False
        if expression[0] == '{':
            cnt = 0
            i = 0
            while i < n:
                if expression[i] == '{':
                    cnt += 1
                elif expression[i] == '}':
                    cnt -= 1
                    if not cnt:
                        break
                i += 1
            if i == n - 1:
                b = True
        if b:
            res = set([])
            cnt = 0
            i0 = i = 1
            while i < n - 1:
                if expression[i] == '{':
                    cnt += 1
                elif expression[i] == '}':
                    cnt -= 1
                elif expression[i] == ',' and cnt == 0:
                    ret = self.braceExpansionII(expression[i0:i])
                    res.update(ret)
                    i0 = i + 1
                i += 1
            ret = self.braceExpansionII(expression[i0:i])
            res.update(ret)
            return sorted(list(res))
        else:
            res = [\"\"]
            i0 = i = 0
            while i < n:
                while i < n and not expression[i] == '{':
                    i += 1
                res = helper(res, [expression[i0:i]])
                i0 = i
                cnt = 0
                while i < n:
                    # print(i, expression[i], cnt)
                    if expression[i] == '{':
                        cnt += 1
                    elif expression[i] == '}':
                        cnt -= 1
                        if not cnt:
                            ret = self.braceExpansionII(expression[i0:(i+1)])
                            res = helper(res, ret)
                            i0 = i + 1
                            break
                    i += 1
            return sorted(list(set(res)))
                
                     
