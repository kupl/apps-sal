class Solution:

    def numSpecialEquivGroups(self, A: List[str]) -> int:
        counter_list = set()
        for i in A:
            even = []
            odd = []
            for (index, item) in enumerate(i):
                if index % 2 == 0:
                    even.append(item)
                else:
                    odd.append(item)
            normalised = ''.join(sorted(even) + sorted(odd))
            counter_list.add(normalised)
        return len(counter_list)
