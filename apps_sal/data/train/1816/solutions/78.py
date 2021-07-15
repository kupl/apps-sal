from collections import defaultdict, deque


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def to_seconds(time):
            h, m = map(int, time.split(\":\"))
            return h*60 + m

        def find_diff(t1, t2):
            t1h, t1m = map(int, t1.split(\":\"))
            t2h, t2m = map(int, t2.split(\":\"))

            t1minutes = t1h * 60 + t1m
            t2minutes = t2h * 60 + t2m

            if t1minutes < t2minutes:
                return float(\"inf\")

            return t1minutes - t2minutes

        keyTime = map(to_seconds, keyTime)

        names = set()
        persons = defaultdict(deque)
        for person, time in sorted(zip(keyName, keyTime), key=lambda x: x[1]):
            persons[person].append(time)
            if len(persons[person]) > 2:
                first_time = persons[person].popleft()
                if time - first_time <= 60:
                    names.add(person)

        return list(sorted(names))

