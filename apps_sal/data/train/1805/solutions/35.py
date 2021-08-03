from collections import deque, defaultdict


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        stack = deque()
        nbr = dict()
        stack.append(id)
        seen = set()
        seen.add(id)
        lvl = 0
        while stack:
            n = len(stack)
            lvl += 1
            if lvl > level:
                break
            for i in range(n):
                person_id = stack.pop()
                for p in friends[person_id]:
                    if p in seen:
                        continue
                    seen.add(p)
                    stack.append(p)
                    if p not in nbr:
                        nbr[p] = lvl

        res = defaultdict(int)
        for person_id in nbr:
            if nbr[person_id] == level:
                for video in watchedVideos[person_id]:
                    res[video] += 1
        res_sorted = sorted(list(res.items()), key=lambda x: (x[1], x[0]))
        return [x[0] for x in res_sorted]
