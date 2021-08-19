class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(list)
        for (node, neigbor) in pairs:
            graph[node].append(neigbor)
            graph[neigbor].append(node)
        visited = set()

        def dfs(index):
            if index not in visited:
                visited.add(index)
                newgroup.add(index)
                for neigbor in graph[index]:
                    dfs(neigbor)
        n = len(s)
        result = [None] * n
        for i in range(n):
            newgroup = set()
            dfs(i)
            subseq = [s[i] for i in newgroup]
            subseq.sort()
            for (letter, index) in zip(subseq, sorted(newgroup)):
                result[index] = letter
        return ''.join(result)
