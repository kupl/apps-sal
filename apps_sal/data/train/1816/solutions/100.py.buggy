class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        pq = []
        for name, time in zip(keyName, keyTime):
            a, b = map(int,time.split(\":\"))
            time = a*60+b
            print(name, time)
            heapq.heappush(pq, (time, name, float('-inf'), 1))
            heapq.heappush(pq, (time+60, name, float('inf'), -1))
            
        cnts = collections.Counter()
        ppl = set()
        while pq:
            time, name, _, c = heapq.heappop(pq)
            cnts[name] += c
            if cnts[name] >= 3:
                ppl.add(name)
        return sorted(list(ppl))
