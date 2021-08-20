class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        max_b_counter = defaultdict(int)
        for word in B:
            word_counter = Counter(word)
            for (char, counter) in list(word_counter.items()):
                max_b_counter[char] = max(max_b_counter[char], word_counter[char])
        result = []
        for word in A:
            word_counter = Counter(word)
            if all([max_b_counter[char] <= word_counter[char] for char in max_b_counter]):
                result.append(word)
        return result
