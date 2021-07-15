class Solution:
    # def findRoot(self, parents, index):
    #     root = index
    #     while parents[root] != root:
    #         root = parents[root]
    #     while root != index:
    #         temp = parents[index]
    #         parents[index] = root
    #         index = temp
    #     return root
    #
    # def creatParents(self, graph):
    #     node_num = len(graph)
    #     parents = [i for i in range(node_num)]
    #     for i in range(node_num):
    #         for j in range(i + 1, node_num):
    #             if graph[i][j] == 1:
    #                 root_i = self.findRoot(parents, i)
    #                 root_j = self.findRoot(parents, j)
    #                 if root_i != root_j:
    #                     parents[root_i] = root_j
    #     return parents
    #
    # def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
    #     initial_num = len(initial)
    #     node_num = len(graph)
    #     if initial_num <= 0 or node_num <= 0:
    #         return 0
    #     if initial_num==1:
    #         return initial[0]
    #
    #     parents = self.creatParents(graph)
    #     node_info = [0] * node_num  # 各节点圈中的节点数
    #     for i in range(node_num):
    #         root = self.findRoot(parents, i)
    #         node_info[root] += 1
    #
    #     # 找出initial种节点圈最大的节点
    #     index = initial[0]
    #     max = -1
    #     for i in range(initial_num):
    #         root = self.findRoot(parents, initial[i])
    #         if node_info[root] > max or (node_info[root] == max and initial[i] < index):
    #             max = node_info[root]
    #             index = initial[i]
    #     return index

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        initial.sort()
        visited = []
        result = [-1, 0]  # index,count

        for i in range(len(graph)):
            if i in visited:
                continue
            else:
                temp = [-1, 0]
                stack = [i]
                visited.append(i)
                stack_num = 1;
                while stack:
                    index = stack.pop(0)
                    if index in initial:
                        if temp[0] == -1:
                            temp[0] = index
                        temp[1] += 1
                    for j in range(len(graph[index])):
                        if graph[index][j] == 1 and (j not in visited):
                            stack.append(j)
                            stack_num += 1
                            visited.append(j)
                if temp[1] == 1:
                    if result[1] < stack_num:
                        result[0] = temp[0]
                        result[1] = stack_num
        return result[0] if result[0] != -1 else initial[0]


