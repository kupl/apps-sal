class TweetCounts:
    SECONDS = {
        \"minute\": 60,
        \"hour\":   60 * 60,
        \"day\":    60 * 60 * 24, 
    }

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)
        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        count = math.ceil((endTime - startTime + 1) / TweetCounts.SECONDS[freq])
        prev = bisect.bisect_left(self.tweets[tweetName], startTime)
        ans = []
        for i in range(1, count+1):
            cur = bisect.bisect_left(self.tweets[tweetName],
                                     min(startTime + i * TweetCounts.SECONDS[freq], endTime+1))
            ans.append(cur - prev)
            prev = cur
        return ans
