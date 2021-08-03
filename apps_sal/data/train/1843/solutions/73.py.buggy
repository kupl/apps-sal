freq_map = {\"minute\": 60, \"hour\": 3600, \"day\": 24*3600}
class TweetCounts:
    def __init__(self):
        self.tweet_dict = {}

    def recordTweet(self, tweetName, time):
        if tweetName not in self.tweet_dict:
            self.tweet_dict[tweetName] = []
        self.tweet_dict[tweetName].append(time)
        
    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        if tweetName not in self.tweet_dict:
            return None
        intervals = (-startTime + endTime)//freq_map[freq] + 1
        
        output = [0]*(intervals)
        for elem in sorted(self.tweet_dict[tweetName]):
            if elem >= startTime and elem <= endTime:
                output[(elem - startTime)//freq_map[freq]] += 1
            if elem > endTime:
                break
        return output

        # Your TweetCounts object will be instantiated and called as such:
        # obj = TweetCounts()
        # obj.recordTweet(tweetName,time)
        # param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

