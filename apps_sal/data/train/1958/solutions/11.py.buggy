class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        
        for person, group_size in enumerate(groupSizes):
            if group_size not in groups:
                groups[group_size] = [[person]]
            else:
                for c_group in groups[group_size]:
                    if len(c_group) < group_size:
                        c_group.append(person)
                        break
                else:
                    groups[group_size].append([person])
        
        
        res = []
        
        [res.extend(v) for v in groups.values()]
        
        return res
                    
        
    
    
\"\"\"

{
    <size>: [[], []]
}


\"\"\"
