class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 1. Generate non-zig path
        path = [label]
        while label != 1:
            label = label // 2
            path.append(label)
        print(path)
        path.reverse()

        odd = len(path) % 2 != 0
        # 2. Account for zig-zag
        for i in range(1, len(path) - 1):
            if not odd and i % 2 == 0:
                print("Here")
                level = [i for i in range(2**(i + 1) - 1, 2**i - 1, -1)]
                index = path[i] - 2**i
                path[i] = level[index]
            elif odd and i % 2 != 0:
                level = [i for i in range(2**(i + 1) - 1, 2**i - 1, -1)]
                index = path[i] - 2**i
                path[i] = level[index]

        return path
