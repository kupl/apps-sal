class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        done = [False for _ in range(n)]
        groups = []
        for i in range(n):
            if done[i]:
                continue
                
                
            numInThisGroup = groupSizes[i]
            peopleInThisGroup = []
            for j in range(n):
                if not done[j] and groupSizes[j] == numInThisGroup:
                    peopleInThisGroup.append(j)
                    if len(peopleInThisGroup) == numInThisGroup:
                        break
                        
            groups.append(peopleInThisGroup)
            for person in peopleInThisGroup:
                done[person] = True
                
        return groups
