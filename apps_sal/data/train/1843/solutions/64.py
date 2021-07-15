class TweetCounts:
    MAP = {
            'minute': 60,
            'hour': 60 * 60,
            'day': 24 * 60 * 60
            }

    def __init__(self):
        self.data = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.data[tweetName].append(time)
        self.data[tweetName].sort()

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        data = self.data[tweetName]
        index = 0

        while index < len(data) and data[index] < startTime:
            index += 1

        ans = []
        tmp = 0
        k = 0
        delta = self.MAP[freq]
        while startTime + k * delta <= endTime:
            end = min(startTime + delta * (k + 1), endTime + 1)
            if index >= len(data) or data[index] >= end:
                ans.append(tmp)
                tmp = 0
                k += 1
            else:
                tmp += 1
                index += 1
        return ans
