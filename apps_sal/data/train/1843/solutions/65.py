from bisect import insort, bisect_left, bisect_right
from math import ceil

class TweetCounts:

    def __init__(self):
        self.tweets={}

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
        ans = [0]*buckets
        start = bisect_left(entry, startTime)
        end = bisect_right(entry, endTime)
        for i in range(start, end):
            time = entry[i]
            d = (time - startTime) // factor
            ans[d] += 1
        return ans
        '''ans=[]
        if freq=='minute':
            q=endTime//60
            p=startTime//60
            for j in range(p,q+1):
                count=0
                for i in range(len(self.tname)):
                    if self.tname[i]==tweetName:
                        if startTime+j*60<=self.t[i]<min(startTime+(j+1)*60,endTime+1):
                            count+=1
                ans.append(count)
        elif freq=='hour':
            q=endTime//3600
            p=startTime//3600
            for j in range(p,q+1):
                count=0
                for i in range(len(self.tname)):
                    if self.tname[i]==tweetName:
                        if startTime+j*3600<=self.t[i]<min(startTime+(j+1)*3600,endTime+1):
                            count+=1
                ans.append(count)
        else:
            q=endTime//(3600*24)
            p=startTime//(3600*24)
            for j in range(p,q+1):
                count=0
                for i in range(len(self.tname)):
                    if self.tname[i]==tweetName:
                        if startTime+j*(24*3600)<=self.t[i]<min(startTime+(j+1)*(3600*24),endTime+1):
                            count+=1
                ans.append(count)
        return ans'''
# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

