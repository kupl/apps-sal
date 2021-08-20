class Solution:

    def maxPower(self, s: str) -> int:
        c = {'power': 1}
        for i in range(len(s)):
            if i == len(s) - 1:
                break
            if ord(s[i]) == ord(s[i + 1]):
                c['power'] += 1
            else:
                c['new start#%s' % i] = c['power']
                c['power'] = 1
        return max(c.values())
