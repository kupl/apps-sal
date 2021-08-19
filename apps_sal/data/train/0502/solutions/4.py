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


# Algorithm

# This algorithm has a few parts:

# Coloring each component: For each node, if it isn't yet colored, use a depth-first search to traverse its component, coloring that component with a new color.

# Size of each color: Count the number of occurrences of each color.

# Find unique colors: Look at the colors of nodes in initial to see which nodes have unique colors.

# Choose answer: For each node with a unique color, find the size of that color. The largest size is selected, with ties broken by lowest node number.

# If there is no node with a unique color, the answer is min(initial).
