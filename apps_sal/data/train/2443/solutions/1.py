class Solution:

    def maxNumberOfBalloons(self, text: str) -> int:
        ret = []
        for i in 'ban':
            ret.append(text.count(i))
        for i in 'lo':
            ret.append(text.count(i) // 2)
        return min(ret)
