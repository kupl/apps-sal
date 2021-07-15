# from collections import deque
# import heapq

# class Solution:
#     def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
#         groups = {}
#         group_counter = 0
        
#         contains_malware = []
#         malware_set = set(initial)
        
#         visited = set()
#         for i in range(len(graph)):
#             group_counter += 1
#             if i not in visited:
#                 queue = deque()
#                 queue.append(i)
#                 while queue:
#                     node = queue.popleft()
#                     visited.add(node)
#                     if node in malware_set:
#                         contains_malware.append((node, group_counter))
#                     if group_counter not in groups:
#                             groups[group_counter] = 1
#                     else:
#                         groups[group_counter] += 1
#                     for candidate_node, flag in enumerate(graph[node]):
#                         if flag == 1 and candidate_node not in visited:
#                             queue.append(candidate_node)
                            
                            
#         if len(initial) == len(graph):
#             individuals = []
#             for node, i in contains_malware:
#                 if groups[i] == 1:
#                     individuals.append(node)
#             individuals.sort()
#             return individuals[0]
#         else:
#             contains_malware = [(-groups[i], node) for node, i in contains_malware]
#             heapq.heapify(contains_malware)
#             return contains_malware[0][1]
                        
import collections
class Solution(object):
    def minMalwareSpread(self, graph, initial):
        # 1. Color each component.
        # colors[node] = the color of this node.

        N = len(graph)
        colors = {}
        c = 0

        def dfs(node, color):
            colors[node] = color
            for nei, adj in enumerate(graph[node]):
                if adj and nei not in colors:
                    dfs(nei, color)

        for node in range(N):
            if node not in colors:
                dfs(node, c)
                c += 1

        # 2. Size of each color.
        # size[color] = number of occurrences of this color.
        size = collections.Counter(list(colors.values()))

        # 3. Find unique colors.
        color_count = collections.Counter()
        for node in initial:
            color_count[colors[node]] += 1

        # 4. Answer
        ans = float('inf')
        for x in initial:
            c = colors[x]
            if color_count[c] == 1:
                if ans == float('inf'):
                    ans = x
                elif size[c] > size[colors[ans]]:
                    ans = x
                elif size[c] == size[colors[ans]] and x < ans:
                    ans = x

        return ans if ans < float('inf') else min(initial)  

