class Solution:

    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        i = int(math.log(label, 2))
        while i >= 1:
            length = pow(2, i + 1) - pow(2, i)
            if i % 2 == 0:
                prev = [j for j in range(int(pow(2, i) - 1), int(pow(2, i - 1) - 1), -1)]
                idx = int(label % length / 2)
            else:
                prev = [j for j in range(int(pow(2, i - 1)), int(pow(2, i)))]
                idx = int((length - 1 - label % length) / 2)
            label = prev[idx]
            ans.append(label)
            i = int(math.log(label, 2))
        ans.sort()
        return ans
