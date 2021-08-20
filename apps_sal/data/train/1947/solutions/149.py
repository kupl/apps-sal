class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        def is_subset(b_dict, a_dict):
            for k in b_dict:
                if k not in a_dict or a_dict[k] < b_dict[k]:
                    return False
            return True

        def get_dict(b):
            counts = {}
            for ch in b:
                counts[ch] = counts.get(ch, 0) + 1
            return counts
        b_dicts = [get_dict(b) for b in B]
        max_b_dict = {}
        for b_dict in b_dicts:
            for key in b_dict:
                max_b_dict[key] = max(max_b_dict.get(key, 0), b_dict[key])
        out = []
        for a in A:
            a_dict = get_dict(a)
            if is_subset(max_b_dict, a_dict):
                out.append(a)
        return out
