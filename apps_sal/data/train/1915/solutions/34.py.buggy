class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        locks = collections.defaultdict(set)
        count_locks = collections.defaultdict(int)
        
        last_window = len(target)-len(stamp)
        
        for i in range(last_window+1):
            for j in range(i, i+len(stamp)):
                if stamp[j-i] != target[j]:
                    locks[j].add(i)
                    count_locks[i] += 1
            
        available_windows = collections.deque([])
        for i in range(last_window+1):
            if count_locks[i] == 0:
                available_windows.append(i)
                
        res = []
        target = list(target)
        while available_windows:
            window = available_windows.popleft()
            res.append(window)
            for i in range(window, window+len(stamp)):
                if target[i] == \"?\":
                    pass
                else:
                    target[i] = \"?\"
                    while locks[i]:
                        w = locks[i].pop()
                        count_locks[w] -= 1
                        if count_locks[w] == 0:
                            available_windows.append(w)
        if any(c != \"?\" for c in target):
            return []
        return res[::-1]
                        
