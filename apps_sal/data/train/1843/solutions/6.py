class TweetCounts:

    def __init__(self):
        # { 'tweet3': [1,3,1000,5]}
        self.__tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self.__tweets:
            self.__tweets[tweetName].append(time)
        else:
            self.__tweets[tweetName] = [time]
        # print(self.__tweets)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        if tweetName not in self.__tweets:
            self.__tweets[tweetName] = []
        
        if freq == \"minute\":
            delta = 60
        elif freq == \"hour\":
            delta = 3600
        else: # day
            assert(freq == \"day\"), freq
            delta = 24*3600
        
        # create intervals:
        nextIntervalStart = startTime
        intervals = []
        intervalCount = 1
        while (endTime+1 > nextIntervalStart):
            nextIntervalEnd = startTime + delta*intervalCount
            intervals.append((nextIntervalStart, min(nextIntervalEnd,endTime+1)))
            nextIntervalStart = nextIntervalEnd
            intervalCount += 1
        
        self.__tweets[tweetName].sort()
        result = []
        index = 0
        for interval in intervals:
            result.append(0)
            while (index < len(self.__tweets[tweetName]) 
                   and self.__tweets[tweetName][index] < interval[1]):
                if self.__tweets[tweetName][index] >= interval[0]:
                    result[-1] += 1
                index += 1
        
        return result


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

# TestCases:
\"\"\"
[\"TweetCounts\",\"recordTweet\",\"recordTweet\",\"recordTweet\",\"getTweetCountsPerFrequency\",\"getTweetCountsPerFrequency\",\"recordTweet\",\"getTweetCountsPerFrequency\"]
[[],[\"tweet3\",0],[\"tweet3\",60],[\"tweet3\",10],[\"minute\",\"tweet3\",0,59],[\"minute\",\"tweet3\",0,60],[\"tweet3\",120],[\"hour\",\"tweet3\",0,210]]

[\"TweetCounts\",\"recordTweet\",\"recordTweet\",\"recordTweet\",\"getTweetCountsPerFrequency\",\"getTweetCountsPerFrequency\",\"recordTweet\",\"getTweetCountsPerFrequency\"]
[[],[\"tweet3\",0],[\"tweet3\",60],[\"tweet3\",10],[\"minute\",\"tweet3\",0,59],[\"minute\",\"tweet3\",0,60],[\"tweet3\",120],[\"day\",\"tweet3\",0,210]]

[\"TweetCounts\",\"recordTweet\",\"recordTweet\",\"recordTweet\",\"getTweetCountsPerFrequency\",\"getTweetCountsPerFrequency\",\"recordTweet\",\"getTweetCountsPerFrequency\"]
[[],[\"tweet3\",0],[\"tweet3\",60],[\"tweet3\",10],[\"minute\",\"tweet3\",0,59],[\"minute\",\"tweet3\",0,60],[\"tweet3\",120],[\"hour\",\"tweet3\",0,0]]

[\"TweetCounts\"]
[[]]

[\"TweetCounts\",\"recordTweet\",\"recordTweet\",\"recordTweet\",\"getTweetCountsPerFrequency\",\"getTweetCountsPerFrequency\",\"recordTweet\",\"getTweetCountsPerFrequency\",\"recordTweet\",\"recordTweet\", \"getTweetCountsPerFrequency\", \"getTweetCountsPerFrequency\"]
[[],[\"tweet3\",0],[\"tweet3\",60],[\"tweet3\",10],[\"minute\",\"tweet3\",0,59],[\"minute\",\"tweet3\",0,30],[\"tweet3\",120],[\"hour\",\"tweet3\",0,210],[\"tweet3\",420],[\"tweet1\",120],[\"minute\",\"tweet3\",0,1000], [\"day\",\"tweet3\",0,500000]]


\"\"\"
