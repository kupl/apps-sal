class Solution:

    def pathInZigZagTree(self, label: int) -> List[int]:
        h = 1
        symmetry = [2]
        while 2 ** h - 1 < label // 2:
            symmetry.append(symmetry[-1] * 2 + 1)
            h += 1
        path = [label]
        while label > 1:
            parent = label >> 1
            label = symmetry[-1] - parent
            path.append(label)
            symmetry.pop()
        return reversed(path)
