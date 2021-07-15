class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = []
        sizes = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in sizes:
                sizes[groupSizes[i]] = [i]
            else:
                sizes[groupSizes[i]].append(i)
        
        for (size, group) in list(sizes.items()):
            for i in range(0, len(group), size):
                groups.append(group[i:i+size])
            
        return groups
           

