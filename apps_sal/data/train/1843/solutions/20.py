class TweetCounts:

    def __init__(self):
        self.data = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.data[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        T, d = self.data[tweetName], 60 if freq == \"minute\" else (3600 if freq == \"hour\" else 86400)
        # ans = [bisect.bisect(T, t+d) - bisect.bisect_left(T, t) for t in range(startTime, endTime, d)]
        ans = [0]*((endTime-startTime)//d + 1)
        if not T or endTime < T[0] or startTime > T[-1]:
            return ans
        i, l = 0, bisect.bisect_left(T, startTime)
        r = bisect.bisect(T, endTime, lo=l)
        #print(\"T, d, l, r, T[l:r], ans:\", T, d, l, r, T[l:r], ans)
        for t in range(startTime+d, endTime+1, d):
            m = bisect.bisect_left(T, t, lo=l, hi=r)
            ans[i] = m-l
            #print(\"i, l, m, ans:\", i, l, m, ans)
            l = m; i += 1
        ans[i] = r-l
        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
