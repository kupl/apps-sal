class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        star = 0
        visited = [False] * len(target)
        target = list(target)
        res = []
        while star < len(target):
            doReplace = False
            for i in range(len(target) - len(stamp) + 1):
                if not visited[i] and self.canReplace(stamp, target, i):
                    star += self.doReplace(stamp, target, i)
                    doReplace = True
                    visited[i] = True
                    res.append(i)
                    if star == len(target):
                        break
            if not doReplace:
                return []
        return res[::-1]

    def canReplace(self, stamp: str, target: List[str], i: int) -> bool:
        for j in range(len(stamp)):
            if target[i] != '*' and stamp[j] != target[i]:
                return False
            i += 1
        return True

    def doReplace(self, stamp: str, target: List[str], i: int) -> int:
        count = 0
        for j in range(len(stamp)):
            if target[i] != '*':
                target[i] = '*'
                count += 1
            i += 1
        return count
