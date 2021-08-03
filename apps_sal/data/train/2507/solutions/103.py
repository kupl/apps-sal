class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        words = [collections.Counter(word) for word in words]

        c = collections.Counter(chars)

        print(words)
        print(c)

        return sum([sum(list(w.values())) for w in words if all([c[i] >= w[i] for i in w])])
