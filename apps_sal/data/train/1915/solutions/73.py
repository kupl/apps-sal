class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n = len(target)
        m = len(stamp)
        totalStamped = 0
        turnStamped = -1
        res = []

        while True:
            turnStamped = 0

            for coverSize in range(m, 0, -1): # size: the window size that will stamp over, so *bc , size = 2, abc , size = 3
                for i in range(m-coverSize+1): # i: the startIdx of \"*\" from left, if left = 0 , then based on m-coverSize, we can figure out rightIdx to add \"*\"
                    newStamp = \"*\"*i + stamp[i:i+coverSize] + \"*\"*(m-coverSize-i)
                    pos = target.find(newStamp)

                    while pos != -1:
                        res.append(pos)
                        turnStamped += coverSize # \"abc\" will cover 3 while \"ab*\" only cover 2
                        target = target[:pos] + \"*\"*len(stamp) + target[pos+len(newStamp):]
                        pos = target.find(newStamp)

            totalStamped += turnStamped
            if turnStamped == 0:
                break

        return res[::-1] if totalStamped == len(target) else []

