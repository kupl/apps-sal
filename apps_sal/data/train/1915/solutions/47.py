class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        from collections import deque, defaultdict
        ls = len(stamp)
        lt = len(target)
        flag = [False] * lt
        todo_mp = defaultdict(set)
        wait_mp = defaultdict(set)
        for i in range(lt - ls + 1):
            for j in range(ls):
                if stamp[j] == target[i + j]:
                    todo_mp[i].add(i + j)
                else:
                    wait_mp[i].add(i + j)
        q = deque([i for i in range(lt - ls + 1) if len(wait_mp[i]) == 0])
        ret = []
        visited = set(q)
        while len(q) > 0 and all(flag) is False:
            idx = q.popleft()
            to_add = False
            for item in todo_mp[idx]:
                if flag[item] is False:
                    flag[item] = True
                    to_add = True
            if to_add is True:
                ret.append(idx)
            for nei in range(max(idx - ls + 1, 0), min(idx + ls - 1, lt - ls) + 1):
                if nei in visited:
                    continue
                for t in todo_mp[idx]:
                    wait_mp[nei].discard(t)
                if len(wait_mp[nei]) == 0:
                    q.append(nei)
                    visited.add(nei)
        if all(flag) is True:
            return ret[::-1]
        return []
