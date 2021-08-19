class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        from random import sample
        adjmat = {}
        for (a, b) in dislikes:
            adjmat[a] = adjmat.get(a, []) + [b]
            adjmat[b] = adjmat.get(b, []) + [a]
        color = {i: -1 for i in range(1, N + 1)}
        unvisited = {i for i in range(1, N + 1)}
        result = True
        while unvisited and result:
            queue = [sample(unvisited, k=1)[0]]
            color[queue[0]] = 1
            while queue and result:
                curr = queue.pop()
                unvisited.discard(curr)
                currcolor = color[curr]
                adjcolor = 0
                if currcolor == 0:
                    adjcolor = 1
                if adjmat.get(curr, 0) == 0:
                    continue
                for i in adjmat[curr]:
                    if i in unvisited:
                        queue.append(i)
                    if color[i] == -1:
                        color[i] = adjcolor
                    elif color[i] == currcolor:
                        result = False
                        break
        return result
