class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(lambda: [])
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        visited = {}

        def visit(index: int, a: int) -> bool:
            if a in visited:
                return (index - visited[a]) % 2 == 0
            visited[a] = index
            for b in graph[a]:
                if not visit(index + 1, b):
                    return False
            return True
        for a in range(1, N + 1):
            if a not in visited and not visit(0, a):
                return False
        return True

    def possibleBipartition1(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0:
            return True
        group1 = defaultdict(lambda: 0)
        group2 = defaultdict(lambda: 0)

        def bothInGroup(group: set, a: int, b: int) -> bool:
            return group[a] > 0 and group[b] > 0

        def helper(group1Person: int, group2Person: int, index: int) -> bool:
            # print(\"helper\", index)
            group1[group1Person] += 1
            group2[group2Person] += 1
            #print(list(filter(lambda x: x[1] > 0, group1.items())))
            #print(list(filter(lambda x: x[1] > 0, group2.items())))
            if index == len(dislikes):
                return True
            a, b = dislikes[index]
            # print(\"loop\", index, a, b)
            if bothInGroup(group1, a, b) or bothInGroup(group2, a, b):
                group1[group1Person] -= 1
                group2[group2Person] -= 1
                return False
            if group1[a] > 0 or group2[b] > 0:
                if helper(a, b, index + 1):
                    return True
            elif group2[a] > 0 or group1[b] > 0:
                if helper(b, a, index + 1):
                    return True
            else:
                if helper(a, b, index + 1):
                    return True
                if helper(b, a, index + 1):
                    return True
            group1[group1Person] -= 1
            group2[group2Person] -= 1
            return False

        return helper(dislikes[0][0], dislikes[0][1], 1)
