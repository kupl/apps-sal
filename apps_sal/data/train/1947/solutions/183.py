class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        counter_b = Counter()
        for b in B:
            for (key, freq) in Counter(b).items():
                counter_b[key] = max(counter_b[key], freq)
        ans = []
        for a in A:
            counter_a = Counter(a)
            for (key, freq) in counter_b.items():
                if counter_a[key] < freq:
                    break
            else:
                ans.append(a)
        return ans
