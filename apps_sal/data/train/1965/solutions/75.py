class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        total_edges = []
        bob_edges = []
        alice_edges = []
        
        
        for (t, x, y) in edges:
            x -= 1
            y -= 1
            if t == 1:
                # bob[x].append(y)
                # bob[y].append(x)
                bob_edges.append((x, y))
            elif t == 2:
                # alice[x].append(y)
                # alice[y].append(x)
                alice_edges.append((x, y))
            else:
                # total[x].append(y)
                # total[y].append(x)
                total_edges.append((x, y))
        
        
        def kruskal(colors, sets, edges):
            used = 0
            for (x, y) in edges:
                if colors[x] == colors[y]:
                    continue

                used += 1
                if len(sets[colors[x]]) < len(sets[colors[y]]):
                    x, y = y, x

                #add y to x
                color_x = colors[x]
                color_y = colors[y]

                for node in sets[color_y]:
                    colors[node] = color_x

                sets[color_x].extend(sets[color_y])
                
            return used
        
        total_colors = list(range(n))
        total_sets = [[i] for i in range(n)]
        
        used_total = kruskal(total_colors, total_sets, total_edges)
        # print(\"New colors\", total_colors)
        
        
        bob_colors = total_colors[::]
        alice_colors = total_colors[::]
        
        bob_sets = [el[::] for el in total_sets]
        alice_sets = [el[::] for el in total_sets]
        
        used_bob = kruskal(bob_colors, bob_sets, bob_edges)
        used_alice = kruskal(alice_colors, alice_sets, alice_edges)
        
        # print(\"Shared uses\", used_total)
        # print(\"Bob used\", used_bob)
        # print(\"Alice used\", used_alice)
        
        if (used_total + used_bob != n - 1) or (used_total + used_alice != n - 1):
            return -1
        
        return len(edges) - used_total - used_bob - used_alice

