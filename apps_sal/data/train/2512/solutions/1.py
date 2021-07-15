class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            state = 0
            real = []
            for c in email:
                if state == 0:
                    if c == '.':
                        continue
                    elif c == '+':
                        state = 1
                    elif c == '@':
                        real.append('@')
                        state = 2
                    else:
                        real.append(c)
                elif state == 1:
                    if c == '@':
                        real.append('@')
                        state = 2
                elif state == 2:
                    real.append(c)
            result.add(''.join(real))
        return len(result)
