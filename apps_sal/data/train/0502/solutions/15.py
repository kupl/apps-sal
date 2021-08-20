class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        initial.sort()
        visited = []
        result = [-1, 0]
        for i in range(len(graph)):
            if i in visited:
                continue
            else:
                temp = [-1, 0]
                stack = [i]
                visited.append(i)
                stack_num = 1
                while stack:
                    index = stack.pop(0)
                    if index in initial:
                        if temp[0] == -1:
                            temp[0] = index
                        temp[1] += 1
                    for j in range(len(graph[index])):
                        if graph[index][j] == 1 and j not in visited:
                            stack.append(j)
                            stack_num += 1
                            visited.append(j)
                if temp[1] == 1:
                    if result[1] < stack_num:
                        result[0] = temp[0]
                        result[1] = stack_num
        return result[0] if result[0] != -1 else initial[0]
