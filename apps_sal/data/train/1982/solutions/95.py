class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        Dislike = collections.defaultdict(list)
        for dislike in dislikes:
            Dislike[dislike[0] - 1].append(dislike[1] - 1)
            Dislike[dislike[1] - 1].append(dislike[0] - 1)
        color = [-1 for i in range(N)]
        while -1 in color:
            uncolored = color.index(-1)
            q = collections.deque([uncolored])
            while q:
                i = q.popleft()
                if color[i] == -1:
                    color[i] = 0
                for d in Dislike[i]:
                    if color[d] == -1:
                        q.append(d)
                        color[d] = color[i] ^ 1
                    elif color[d] == color[i]:
                        return False
        return True
