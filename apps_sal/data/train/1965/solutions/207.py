from collections import defaultdict


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 1、关于两个人的连通性考察， O（N）
        # 2、开始移除 有type3和其他的边重复，优先移除其他的
        # 3、去掉type3组成的环（用节点数和边的数量关系来计算需要去除多少个多余的边）
        # 4、然后单独考察每个人的重复边（用边和节点数量关系计算）
        count = 0
        type3 = set()
        adj3 = defaultdict(list)
        for edge in edges:
            edge_type, node1, node2 = edge
            if edge_type == 3:
                type3.add((node1, node2))
                adj3[node1].append(node2)
                adj3[node2].append(node1)

        type1, type2 = set(), set()
        adj1, adj2 = defaultdict(list), defaultdict(list)
        for edge in edges:
            edge_type, node1, node2 = edge
            if edge_type == 3:
                continue
            if (node1, node2) in type3 or (node2, node1) in type3:
                count += 1
                continue
            if edge_type == 1:
                type1.add((node1, node2))
                adj1[node1].append(node2)
                adj1[node2].append(node1)
            elif edge_type == 2:
                type2.add((node1, node2))
                adj2[node1].append(node2)
                adj2[node2].append(node1)

        # 连通性考察
        visited = set(range(1, n + 1))
        queue = [1]
        while queue and visited:
            new_queue = []
            while queue:
                curr = queue.pop()
                if curr in visited:
                    visited.remove(curr)
                    for node in adj1[curr] + adj3[curr]:
                        if node in visited:
                            new_queue.append(node)
            queue = new_queue
        if visited:  # 说明不能遍历
            return -1
        visited = set(range(1, n + 1))
        queue = [1]
        while queue and visited:
            new_queue = []
            while queue:
                curr = queue.pop()
                if curr in visited:
                    visited.remove(curr)
                    for node in adj2[curr] + adj3[curr]:
                        if node in visited:
                            new_queue.append(node)
            queue = new_queue
        if visited:  # 说明不能遍历
            return -1

        # type3, adj3
        # 需要在搜索过程中同时记录边和节点
        used = set()
        for node1, node2 in type3:
            if node1 in used:
                continue
            edge_record = set()
            node_record = set()
            queue = [node1]
            while queue:
                new_queue = []
                while queue:
                    curr = queue.pop()
                    used.add(curr)
                    node_record.add(curr)
                    for node in adj3[curr]:
                        if node in used:
                            continue
                        if (curr, node) in type3:
                            edge_record.add((curr, node))
                        else:
                            edge_record.add((node, curr))
                        new_queue.append(node)
                queue = new_queue
            count -= len(edge_record) - len(node_record) + 1

        # 去除type3的环
        return count + len(type1) + len(type3) - n + 1 + len(type2) + len(type3) - n + 1
