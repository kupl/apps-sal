class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        groups = []
        cache = {}

        for i in range(len(groupSizes)):
            if groupSizes[i] not in cache:
                cache[groupSizes[i]] = []

            if len(cache[groupSizes[i]]) < groupSizes[i]:
                cache[groupSizes[i]].append(i)

            if len(cache[groupSizes[i]]) == groupSizes[i]:
                groups.append(cache[groupSizes[i]])
                cache.pop(groupSizes[i])

        return groups
