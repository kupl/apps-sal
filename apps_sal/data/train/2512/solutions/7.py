class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        out = set()
        for email in emails:
            ar = email.split('@')
            out.add(ar[0].split('+')[0].replace('.', '') + '@' + ar[1])
        return len(out)
