class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            newemail = []
            afterplus = False
            afterat = False
            for ch in email:
                if afterat:
                    newemail.append(ch)
                elif ch == '.':
                    pass
                elif ch == '+':
                    afterplus = True
                elif ch == '@':
                    newemail.append(ch)
                    afterat = True
                elif not afterplus:
                    newemail.append(ch)
            emailSet.add(''.join(newemail))
        return len(emailSet)
