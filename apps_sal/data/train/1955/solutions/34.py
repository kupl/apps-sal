class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return s

        adj_list = {}
        visited = set()
        sub_string = ''
        sub_indices = []

        for i in range(len(pairs)):
            adj_list[pairs[i][0]] = adj_list.get(pairs[i][0], []) + [pairs[i][1]]
            adj_list[pairs[i][1]] = adj_list.get(pairs[i][1], []) + [pairs[i][0]]

        def dfs(index):
            nonlocal sub_string
            sub_string += s[index]
            sub_indices.append(index)
            visited.add(index)

            if index in adj_list:
                for neighbor in adj_list[index]:
                    if neighbor not in visited:
                        dfs(neighbor)

        for i in range(len(s)):
            sub_string = ''
            sub_indices = []
            if i not in visited:
                dfs(i)
                sub_string = sorted(sub_string)
                sub_indices.sort()

                for i in range(len(sub_indices)):
                    s = s[:sub_indices[i]] + sub_string[i] + s[sub_indices[i] + 1:]

        return s
