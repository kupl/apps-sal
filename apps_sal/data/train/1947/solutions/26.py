class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        answer = list()
        b_counter = collections.Counter()
        for word in B:
            counter = collections.Counter(word)
            for letter, count in counter.items():
                b_counter[letter] = max(b_counter[letter], count)

        for word in A:
            counter = collections.Counter(word)
            if all(l in counter and counter[l] >= count for l, count in b_counter.items()):
                answer.append(word)

        return answer
