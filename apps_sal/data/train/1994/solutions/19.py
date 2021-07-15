# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        # construct the graph
        graph = collections.defaultdict(dict)
        
        for node in G:
            graph[node][node] = True
        
        while head:
            # have a edge
            if head.__next__ and head.val in graph and head.next.val in graph:
                graph[head.val][head.next.val] = True
                graph[head.next.val][head.val] = True
            head = head.__next__
        print(graph)
        # Find connected components, by BFS
        result, queue, visited = 0, collections.deque(), set()
        
        for g in graph:
            if g not in visited:
                queue.append(g)
                result += 1
                while queue:
                    node = queue.pop()
                    visited.add(node)
                    neighbors = graph[node]
                    for nei in neighbors:
                        if nei not in visited:
                            queue.append(nei)
        return result
    
    

