class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        output = []

        for i in range(len(groupSizes)):
            belongGroupCount = groupSizes[i]

            existingGroup = groups.get(belongGroupCount)
            if existingGroup is None:
                groups[belongGroupCount] = []
                existingGroup = groups.get(belongGroupCount)

            existingGroup.append(i)
            if len(existingGroup) == belongGroupCount:
                output.append(existingGroup)
                groups[belongGroupCount] = []
            else:
                groups[belongGroupCount] = existingGroup

        return output
