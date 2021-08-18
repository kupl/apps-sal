class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def get_color(u):
            out = colors[u]
            if out != u:
                out = get_color(out)
                colors[u] = out
            return out

        ans = 0
        colors = [i for i in range(n + 1)]
        edges_3 = 0
        for one in edges:
            if one[0] == 3:
                u_color = get_color(one[1])
                v_color = get_color(one[2])

                if u_color == v_color:
                    ans += 1
                else:
                    edges_3 += 1
                    colors[v_color] = u_color

        colors2 = list(colors)
        edges_count = edges_3
        for one in edges:
            if one[0] == 1:
                u_color = get_color(one[1])
                v_color = get_color(one[2])
                if u_color == v_color:
                    ans += 1
                else:
                    edges_count += 1
                    colors[v_color] = u_color

        if edges_count < n - 1:
            return -1

        colors = colors2
        edges_count = edges_3
        for one in edges:
            if one[0] == 2:
                u_color = get_color(one[1])
                v_color = get_color(one[2])
                if u_color == v_color:
                    ans += 1
                else:
                    edges_count += 1
                    colors[v_color] = u_color

        if edges_count < n - 1:
            return -1

        return ans
