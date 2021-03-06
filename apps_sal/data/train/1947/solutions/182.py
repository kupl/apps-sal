class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_counters = [Counter(b_str) for b_str in B]
        common_counter = defaultdict(int)
        for b_cnt in b_counters:
            for (b_let, b_let_cnt) in b_cnt.items():
                common_counter[b_let] = max(common_counter[b_let], b_let_cnt)
        result = []
        for a_str in A:
            a_cnt = Counter(a_str)
            if all((a_cnt.get(c_let, 0) >= c_let_cnt for (c_let, c_let_cnt) in common_counter.items())):
                result.append(a_str)
        return result
