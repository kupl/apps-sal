class TweetCounts:

    def __init__(self):
        self.log = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.log[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        ret = []
        events = sorted([t for t in self.log[tweetName] if startTime <= t <= endTime])
        ei = 0
        time = startTime
        delta = {'minute': 60, 'hour': 3600, 'day': 24 * 3600}[freq]
        cur = 0
        while time <= endTime:
            if ei == len(events):
                ret.append(cur)
                cur = 0
                time += delta
                continue
            if events[ei] < time:
                ei += 1
            elif time + delta <= events[ei]:
                ret.append(cur)
                time += delta
                cur = 0
            else:
                assert time <= events[ei] < time + delta
                cur += 1
                ei += 1
        return ret
