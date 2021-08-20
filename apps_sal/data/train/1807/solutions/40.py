class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:
        added = set()
        result = []
        for denominator in range(2, n + 1):
            for i in range(1, denominator):
                if i / denominator in added:
                    continue
                added.add(i / denominator)
                result.append(f'{i}/{denominator}')
        return result
