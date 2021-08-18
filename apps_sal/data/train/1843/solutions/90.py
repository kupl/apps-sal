class TweetCounts:

    def __init__(self):
        self.tweetDict = {}

    def insertAt(self, tN, x):
        l = 0
        r = len(self.tweetDict[tN]) - 1
        if x < self.tweetDict[tN][l]:
            return 0
        if x > self.tweetDict[tN][r]:
            return r + 1
        while r > l:
            m = (r + l) // 2
            if self.tweetDict[tN][m] < x:
                l = m + 1
            else:
                r = m
        return l

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self.tweetDict:
            self.tweetDict[tweetName].insert(self.insertAt(tweetName, time), time)
        else:
            self.tweetDict[tweetName] = [time]

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        ans = []
        if freq == 'minute':
            delta = 60
        elif freq == 'hour':
            delta = 3600
        else:
            delta = 86400
        total = (endTime - startTime) // delta
        if (endTime - startTime) % delta > 0:
            total += 1
        n = 0
        for t in range(startTime, endTime + 1, delta):
            t0 = t
            t1 = min(t + delta, endTime + 1)
            i0 = self.insertAt(tweetName, t0)
            if i0 == len(self.tweetDict[tweetName]):
                ans += [0] * (total - n)
                return ans
            i1 = self.insertAt(tweetName, t1)
            if i1 == len(self.tweetDict[tweetName]):
                ans.append(i1 - i0)
                ans += [0] * (total - n - 1)
                return ans
            n += 1
            ans.append(i1 - i0)
        return ans
