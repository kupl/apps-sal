class TweetCounts:

    def __init__(self):
        self.data = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.data[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq[0]=='m':
            ans = [0]*((endTime-startTime)//60 +1)
            for x in self.data[tweetName]:
                if startTime<=x<=endTime:
                    a = (x-startTime)//60
                    ans[a]+=1
            return ans
            
        elif freq[0]=='h':
            ans = [0]*((endTime-startTime)//3600 +1)
            for x in self.data[tweetName]:
                if startTime<=x<=endTime:
                    a = (x-startTime)//3600
                    ans[a]+=1
            return ans
        else:
            ans = [0]*((endTime-startTime)//86400 +1)
            for x in self.data[tweetName]:
                if startTime<=x<=endTime:
                    a = (x-startTime)//86400
                    ans[a]+=1
            return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

