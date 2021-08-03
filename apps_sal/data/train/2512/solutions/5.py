class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailDict = {}
        total = 0
        for email in emails:
            domain = email.split('@')[1]
            localPart = email.split('@')[0]
            localPart = localPart.split('+')[0]
            localPart = localPart.replace('.', '')

            if domain not in emailDict:
                emailDict[domain] = set({localPart})
                total += 1
            elif localPart not in emailDict[domain]:
                emailDict[domain].add(localPart)
                total += 1

        return total
