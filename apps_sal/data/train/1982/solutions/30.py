class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        (NOT_COLORED, BLUE, GREEN) = (0, 1, -1)
        if N == 1 or not dislikes:
            return True
        dislike_table = collections.defaultdict(list)
        color_table = [NOT_COLORED for _ in range(N + 1)]
        for (i, j) in dislikes:
            dislike_table[i].append(j)
            dislike_table[j].append(i)

        def dfs(node, color):
            color_table[node] = color
            for adj in dislike_table[node]:
                if color_table[adj] == color:
                    return False
                if color_table[adj] == NOT_COLORED and (not dfs(adj, -color)):
                    return False
            return True
        for person_id in range(1, N + 1):
            if color_table[person_id] == NOT_COLORED and (not dfs(person_id, BLUE)):
                return False
        return True
