class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:

        groups = []

        def match(string):

            odds, evens = {}, {}

            for i in range(0, len(string), 2):
                evens[string[i]] = evens.get(string[i], 0) + 1

            for i in range(1, len(string), 2):
                odds[string[i]] = odds.get(string[i], 0) + 1

            for g in groups:
                if g[0] == odds and g[1] == evens:
                    return True, odds, evens

            return False, odds, evens

        for s in A:

            matched, odds, evens = match(s)

            if not matched:
                groups.append((odds, evens))

        return len(groups)
