from collections import defaultdict, deque


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 1、移除type3的重复边
        # 2、检查alice和bob的可遍历性
        # 3、检查type3组成的环
        # 4、检查alice type1组成的环
        # 5、检查bob type2组成的环
        count = 0
        set1, set2, set3 = set(), set(), set()
        adj_a, adj_b, adj_3 = defaultdict(set), defaultdict(set), defaultdict(set)
        for edge in edges:
            tp, i, j = edge
            if tp == 3:
                set3.add((i, j))
                adj_3[i].add(j)
                adj_3[j].add(i)
                adj_a[i].add(j)
                adj_a[j].add(i)
                adj_b[i].add(j)
                adj_b[j].add(i)

        for edge in edges:
            tp, i, j = edge
            if tp != 3:
                if ((i, j) in set3 or (j, i) in set3):
                    count += 1
                elif tp == 1:
                    set1.add((i, j))
                    adj_a[i].add(j)
                    adj_a[j].add(i)
                elif tp == 2:
                    set2.add((i, j))
                    adj_b[i].add(j)
                    adj_b[j].add(i)

        def is_traversable(adj):
            visited = set()
            queue = deque([1])
            while queue:
                root = queue.popleft()
                visited.add(root)
                for i in adj[root]:
                    if i not in visited:
                        queue.append(i)
            if len(visited) != n:
                return False
            else:
                return True

        if not is_traversable(adj_a) or not is_traversable(adj_b):
            return -1

        dup_3 = 0
        visited = set()
        for edge in set3:
            if edge in visited:
                continue
            node_set = set()
            edge_set = set()
            i, j = edge
            queue = deque([i])
            while queue:
                root = queue.popleft()
                node_set.add(root)
                for k in adj_3[root]:
                    if k not in node_set:
                        queue.append(k)
                        if (root, k) in set3:
                            edge_set.add((root, k))
                        else:
                            edge_set.add((k, root))

            dup_3 += len(edge_set) - len(node_set) + 1
            for v_edge in edge_set:
                visited.add(v_edge)

        type3_count = len(set3) - dup_3
        return count + len(set1) + 2 * type3_count - n + 1 + len(set2) - n + 1 + dup_3
