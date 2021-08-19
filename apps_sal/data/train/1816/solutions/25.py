from sortedcontainers import SortedList


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        alerted_workers = set()
        worker_enter = {}
        for (name, time) in zip(keyName, keyTime):
            if name in alerted_workers:
                continue
            time = int(time[:2]) * 60 + int(time[-2:])
            if not name in worker_enter:
                worker_enter[name] = SortedList()
            if len(worker_enter[name]) >= 2:
                index = worker_enter[name].bisect(time)
                if index - 2 >= 0 and time - worker_enter[name][index - 2] <= 60 or (index - 1 >= 0 and index < len(worker_enter[name]) and (worker_enter[name][index] - worker_enter[name][index - 1] <= 60)) or (index + 1 < len(worker_enter[name]) and worker_enter[name][index + 1] - time <= 60):
                    alerted_workers.add(name)
            worker_enter[name].add(time)
        return list(sorted(alerted_workers))
