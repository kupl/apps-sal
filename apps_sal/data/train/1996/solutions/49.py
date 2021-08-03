class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def cycle(snode):
            if mem[snode] == -1:
                return True
            elif mem[snode] == 1:
                return False

            seen_path.add(snode)
            for e in graph[snode]:
                if e in seen_path:
                    for n in seen_path:
                        mem[n] = -1
                    return True
                if e not in seen:
                    seen.add(e)
                    res = cycle(e)
                    if res:
                        return res
            mem[snode] = 1
            seen_path.discard(snode)
            return False

        ret = []
        seen = set()
        seen_path = set()
        mem = [0] * len(graph)
        for i in range(len(graph)):
            seen_path.clear()
            seen.clear()
            if not cycle(i):
                ret.append(i)
        return ret
