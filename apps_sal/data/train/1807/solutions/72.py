class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:
        out = []
        visited = set()
        if n == 1:
            return out
        for i in range(2, n + 1):
            for j in range(1, i):
                tmp = f'{j}/{i}'
                if eval(tmp) not in visited:
                    visited.add(eval(tmp))
                    out.append(tmp)
        return out
