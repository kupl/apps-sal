class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        count = collections.Counter()
        for b in B:
            # 两个Counter求或就是每一个元素key都更新到最大值。
            count = count | collections.Counter(b)
            # 两个Counter求与就是每一个元素key都更新到最小值。
        return [a for a in A if Counter(a) & count == count]
