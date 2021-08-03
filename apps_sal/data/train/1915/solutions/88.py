class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        s = set([stamp])
        for i in range(len(stamp)):
            for j in range(len(stamp), i, -1):
                s.add('*' * i + stamp[i:j] + '*' * (len(stamp) - j))
        print(s)

        turns = 0
        numStars = 0
        ans = []
        while turns <= 10 * len(target) and numStars != len(target):
            # print(target)
            replaced = False
            numStars = 0
            for i in range(len(target)):
                if target[i] == '*':
                    numStars += 1
                if i >= len(target) - len(stamp) + 1:
                    continue
                if target[i:i + len(stamp)] in s:
                    ans.append(i)
                    replaced = True
                    target = target[:i] + '*' * len(stamp) + target[i + len(stamp):]
                    break
            if not replaced and numStars != len(target):
                return []
            turns += 1

        if turns <= 10 * len(target):
            ans.reverse()
            return ans
        else:
            return []
