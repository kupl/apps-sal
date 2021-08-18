class TweetCounts:

    def __init__(self):
        self.a = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        heapq.heappush(self.a[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.a:
            return []
        temp = list(self.a[tweetName])
        q = []
        while temp:
            q.append(heapq.heappop(temp))
        if freq == 'minute':
            f = 60
        elif freq == 'hour':
            f = 3600
        else:
            f = 3600 * 24

        bucket_size = (endTime - startTime) // f + 1
        ans = [0] * bucket_size
        cur = 0
        end = f + startTime
        for t in q:
            if t < startTime:
                continue
            if t > endTime:
                break
            i = (t - startTime) // f
            ans[i] += 1

        return ans
