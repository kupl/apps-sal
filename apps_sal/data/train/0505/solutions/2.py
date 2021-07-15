class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # ())()
        # (()
        # (()()
        # ()(()
        
        # Strategy: If sum over string at any point is negative, remove close paren immediately
        #           Keep track of open parens in string. If sum returns to 0, forget parens and restart, since this is valid so far.
        #           At the end remove (sum of string) parens from beginning.
        
        # s = lee(t(c)o)de)
        # total = 0
        # new_s = 
        # recent_opens = []
        
        total = 0
        new_s = ''
        recent_opens = []  # List of indices in new_s of open parens
        for char in s:
            if char == '(':
                total += 1
                new_s = ''.join((new_s, char))

                recent_opens.append(len(new_s) - 1)
            elif char == ')':
                total -= 1

                if total >= 0:
                    new_s = ''.join((new_s, char))
                    recent_opens.pop()
                    
                else:
                    total = 0
                    
            else:
                new_s = ''.join((new_s, char))     

        # Remove extra open parens, if any
        if total > 0:
            for count, index in enumerate(recent_opens):
                total -= 1
                
                new_s = ''.join((new_s[:index - count], new_s[index - count + 1:]))
                
                if total <= 0:
                    break
                    
        return new_s
