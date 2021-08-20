class Solution:

    def pathInZigZagTree(self, label: int) -> List[int]:
        x = bin(label)[2:]
        n = len(x)
        out = []
        y = '1'
        for i in range(1, n):
            y += '0' if x[i] == '1' else '1'
        for i in range(n):
            if n % 2 == 0:
                if i % 2 == 1:
                    out.append(int(x[:i + 1], 2))
                else:
                    out.append(int(y[:i + 1], 2))
            elif i % 2 == 0:
                out.append(int(x[:i + 1], 2))
            else:
                out.append(int(y[:i + 1], 2))
        return out
