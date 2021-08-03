class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def toMinutes(time):
            hour, minute = time.split(':')
            return int(hour) * 60 + int(minute)

        book = collections.defaultdict(list)
        n = len(keyName)
        res = set()
        for i in range(n):
            q = book[keyName[i]]
            time = toMinutes(keyTime[i])
            heapq.heappush(q, time)
        for k, v in list(book.items()):
            window = collections.deque()
            while v:
                window.append(heapq.heappop(v))
                if len(window) >= 3 and (window[-1] - window[0]) <= 60:
                    res.add(k)
                while window and window[-1] - window[0] > 60:
                    window.popleft()
                #print(k, window)

        return sorted(res)
