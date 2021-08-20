class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_union_ctr = Counter()
        for b_element in B:
            b_union_ctr |= Counter(b_element)
        output = []
        for a_element in A:
            a_count = Counter(a_element)
            if len(b_union_ctr - a_count) == 0:
                output.append(a_element)
        return output
