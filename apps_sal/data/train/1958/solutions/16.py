class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        memory = {}
        for i, el in enumerate(groupSizes):
            if el not in memory:
                memory[el] = [[i]]
            else:
                next_available = None
                for j in range(len(memory[el])):
                    if len(memory[el][j]) < el:
                        next_available = j

                if next_available is None:
                    memory[el].append([i])
                else:
                    memory[el][next_available].append(i)

        res = []
        for groups in memory.values():
            res.extend(groups)
        return res
