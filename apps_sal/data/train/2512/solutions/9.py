class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        final = set()
        for email in emails:
            first, second = email.split('@')
            if '+' in first:
                first = first.split('+')
                f = [i for i in first[0] if i != '.']
            else:
                f = [i for i in first if i != '.']
            final.add(''.join(f) + '@' + second)

        return len(final)
