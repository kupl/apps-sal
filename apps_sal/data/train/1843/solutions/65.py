from bisect import insort, bisect_left, bisect_right
from math import ceil


class TweetCounts:

    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets:
            self.tweets[tweetName] = []
        insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        entry = self.tweets[tweetName]
        diff = endTime - startTime
        factor = 86400
        if freq == 'minute':
            factor = 60
        elif freq == 'hour':
            factor = 3600
        buckets = math.ceil((diff + 1) / factor)
        ans = [0] * buckets
        start = bisect_left(entry, startTime)
        end = bisect_right(entry, endTime)
        for i in range(start, end):
            time = entry[i]
            d = (time - startTime) // factor
            ans[d] += 1
        return ans
        "ans=[]\n        if freq=='minute':\n            q=endTime//60\n            p=startTime//60\n            for j in range(p,q+1):\n                count=0\n                for i in range(len(self.tname)):\n                    if self.tname[i]==tweetName:\n                        if startTime+j*60<=self.t[i]<min(startTime+(j+1)*60,endTime+1):\n                            count+=1\n                ans.append(count)\n        elif freq=='hour':\n            q=endTime//3600\n            p=startTime//3600\n            for j in range(p,q+1):\n                count=0\n                for i in range(len(self.tname)):\n                    if self.tname[i]==tweetName:\n                        if startTime+j*3600<=self.t[i]<min(startTime+(j+1)*3600,endTime+1):\n                            count+=1\n                ans.append(count)\n        else:\n            q=endTime//(3600*24)\n            p=startTime//(3600*24)\n            for j in range(p,q+1):\n                count=0\n                for i in range(len(self.tname)):\n                    if self.tname[i]==tweetName:\n                        if startTime+j*(24*3600)<=self.t[i]<min(startTime+(j+1)*(3600*24),endTime+1):\n                            count+=1\n                ans.append(count)\n        return ans"
