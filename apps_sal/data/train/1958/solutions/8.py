class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        output = []

        for i in range(len(groupSizes)):
            belongGroupCount = groupSizes[i]
            # print(f'group: {belongGroupCount} | person i: {i}')

            existingGroup = groups.get(belongGroupCount)
            # print(f'existing: {groups}, belong: {belongGroupCount}')
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
