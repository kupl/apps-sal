class Solution:

    def watchedVideosByFriends(self, videos: List[List[str]], friends: List[List[int]], me: int, level: int) -> List[str]:
        visit = set()
        (queue, arr) = ([me], [])
        while level:
            level -= 1
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                if curr not in visit:
                    visit.add(curr)
                    for f in friends[curr]:
                        queue.append(f)
        v = []
        for i in queue:
            if i not in visit:
                visit.add(i)
                v += videos[i]
        c = collections.Counter(v)
        return sorted(sorted(list(set(v))), key=lambda x: c[x])
