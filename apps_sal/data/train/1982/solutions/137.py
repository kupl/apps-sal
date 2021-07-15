class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        graph = {i: set() for i in range(1, N + 1)}
        for u, v in dislikes:
            graph[u].add(v)
            graph[v].add(u)

        colours = {}

        for u in graph:
            colours.setdefault(u, False)

            st = [u]
            while st:
                a = st.pop()
                ca = colours[a]

                for v in graph[a]:
                    cv = colours.get(v)
                    if cv is not None:
                        if cv == ca:
                            return False
                    else:
                        colours[v] = not ca
                        st.append(v)
        return True
