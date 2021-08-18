class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]
        ans = []
        for i in range(50):
            if (2**i <= label) and (2**(i + 1) - 1 >= label):
                break
        if i % 2 == 1:
            label = 2**i + 2**(i + 1) - 1 - label
        x = label
        for j in range(i, -1, -1):
            if j % 2 == 1:
                ans.append(2**j + 2**(j + 1) - 1 - x)
            else:
                ans.append(x)
            x = x // 2

        return ans[::-1]
