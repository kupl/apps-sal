import collections


class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        krem = set(range(len(friends)))
        krem.remove(id)
        curlevel = 0
        klevel = set([id])
        while True:
            if curlevel == level:
                break
            newlevel = set()
            for pid in klevel:
                for fid in friends[pid]:
                    if not fid in krem:
                        continue
                    krem.remove(fid)
                    newlevel.add(fid)
            klevel = newlevel
            curlevel += 1
        krem = None
        vids = collections.defaultdict(int)
        for pid in klevel:
            for vid in watchedVideos[pid]:
                vids[vid] += 1
        return [x[0] for x in sorted(vids.items(), key=lambda x: (x[1], x[0]))]
